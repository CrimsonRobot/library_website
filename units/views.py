from .models import Tree
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.db.models.expressions import RawSQL
from django.shortcuts import render
from django.utils.html import escape
from staff.models import StaffPage, StaffPageSubjectPlacement
from subjects.models import Subject
from units.models import UnitIndexPage, UnitPage
from units.utils import get_quick_nums_for_library_or_dept
from wagtail.wagtailimages.models import Image
from public.models import StandardPage, LocationPage
from library_website.settings import PUBLIC_HOMEPAGE, QUICK_NUMS, REGENSTEIN_HOMEPAGE, SSA_HOMEPAGE, MANSUETO_HOMEPAGE, CRERAR_HOMEPAGE, ECKHART_HOMEPAGE, DANGELO_HOMEPAGE, SCRC_HOMEPAGE
from base.utils import get_hours_and_location, get_page_loc_name
from ask_a_librarian.utils import get_chat_status, get_chat_status_css, get_unit_chat_link
from django.utils.text import slugify
import urllib.parse

'''
"subject" means a subject and all of it's descendants.
"department" means the Unit Page and all of its descendants. .get_descendants(True)

for each subject, check to see there are any entries in the staffpage subject placement table that contain those staff. if so, this one is ok. 
'''
def get_subjects():
    placed_subjects_and_descendants = set(StaffPageSubjectPlacement.objects.all().values_list('subject__name', flat=True))
    subjects = []
    for s in Subject.objects.filter(display_in_dropdown=True):
        dropdown_subject_and_descendants = set(s.get_descendants(True).values_list('name', flat=True))
        if placed_subjects_and_descendants.intersection(dropdown_subject_and_descendants):
            subjects.append(s.name)
    return subjects

def get_staff_pages_for_library(library = None):
    all_staff = StaffPage.objects.live().order_by('last_name', 'first_name')
    if library:
        # see units.models.BUILDINGS
        library_name_to_building = {
            get_page_loc_name(ECKHART_HOMEPAGE): 3,
            get_page_loc_name(CRERAR_HOMEPAGE): 1,
            get_page_loc_name(DANGELO_HOMEPAGE): 2,
            get_page_loc_name(SSA_HOMEPAGE): 7,
            LocationPage.objects.live().get(id=REGENSTEIN_HOMEPAGE).title: 5,
            get_page_loc_name(SCRC_HOMEPAGE): 6,
            get_page_loc_name(MANSUETO_HOMEPAGE): 4
        }
        try:
            building = library_name_to_building[library]
            return StaffPage.objects.filter(staff_page_units__library_unit__building=building).order_by('last_name', 'first_name')
        except:
            return all_staff 
    else:
        return all_staff

def get_staff_pages_for_unit(unit_page_full_name = None, recursive = False, display_supervisor_first = False):
    unit_page_ids = None
    unit_page = None
    if unit_page_full_name:
        for u in UnitPage.objects.live():
            if u.get_full_name() == unit_page_full_name:
                unit_page = u
                if recursive:
                    unit_page_ids = list(u.get_descendants(True).values_list('id', flat=True))
                else:
                    unit_page_ids = [u.id]
                break

    if unit_page_ids == None:
        recursive = True
        unit_page_ids = list(UnitIndexPage.objects.first().get_descendants(True).values_list('id', flat=True))
  
    staff_pages = StaffPage.objects.live().filter(staff_page_units__library_unit__id__in=unit_page_ids).order_by('last_name', 'first_name')
    
    if display_supervisor_first:
        if unit_page and unit_page.department_head:
            staff_pages = [unit_page.department_head] + list(staff_pages.exclude(id=unit_page.department_head.id))
        
    return staff_pages

def units(request):
    def get_unit_info_from_unit_page(unit_page):
        h = ''
        # phone number
        for unit_page_phone_number in unit_page.unit_page_phone_number.all():
            if unit_page_phone_number.phone_label:
                h = h + '<em>' + unit_page_phone_number.phone_label + ':' + '</em> '
            if unit_page_phone_number.phone_number:
                h = h + "<a href='tel:" + unit_page_phone_number.phone_number.replace('-', '') + "'>" + unit_page_phone_number.phone_number + "</a>"
            h = h + '<br/>'

        # fax_number  
        if unit_page.fax_number:
            h = h + 'Fax: ' + unit_page.fax_number + '<br/>'

        # email_label, email
        if unit_page.email:
            if unit_page.email_label:
                h = h + "<a href='mailto:" + unit_page.email + "'>" + unit_page.email_label + "</a><br/>"
            else:
                h = h + "<a href='mailto:" + unit_page.email + "'>" + unit_page.email + "</a><br/>"

        # link_text, link_external, link_page, link_document
        url = ''
        if unit_page.link_external:
            url = unit_page.link_external
        elif unit_page.link_page:
            url = unit_page.link_page.url
        elif unit_page.link_document:
            url =  unit_page.link_document.url

        if url:
            if unit_page.link_text:
                link_text = unit_page.link_text
            else:
                link_text = url
            h = h + "<a href='" + url + "'>" + link_text + "</a><br/>"

        return h

    def get_unit_info(t):
        h = ''

        # intercept this in the future to link to unit pages. 
        staff_link = ''
        if StaffPage.objects.filter(staff_page_units__library_unit=t.unit_page).exists():
            staff_link = " <a href='/about/directory/?" + urllib.parse.urlencode({'view': 'staff', 'department': t.unit_page.get_full_name()}) + "'>staff</a>"

        room_number = ''
        if t.unit_page.room_number:
            room_number = " (" + t.unit_page.room_number + ") "

        if t.name:
            directory_name = t.name
            if t.unit_page.public_web_page:
                directory_name = '<a href="' + t.unit_page.public_web_page.url + '">' + directory_name + '</a>'
            
            h = h + "<strong>" + directory_name + room_number + staff_link + "</strong><br/>"

        if t.unit_page:
            h = h + get_unit_info_from_unit_page(t.unit_page)

        if h:
            h = '<p>' + h + '</p>'
        return h
        
    # hierarchical html. e.g.,
    # <ul>
    #   <li>Administration</li>
    #   <li>Collection Services
    #      <ul>
    #         <li>Administration</li>
    # ...
    def get_html(tree):
        if not tree:
            return ''
        else:
            return "<ul>" + "".join(list(map(lambda t: "<li>" + get_unit_info(t) + get_html(t) + "</li>", tree.children))) + "</ul>"

    # 
    # MAIN
    #

    hierarchical_html = ''
    
    department = request.GET.get('department', None)
    library = request.GET.get('library', None)
    page = request.GET.get('page', 1)
    query = request.GET.get('query', None)
    sort = request.GET.get('sort', 'hierarchical')
    subject = request.GET.get('subject', None)
    view = request.GET.get('view', 'department')

    if library == 'The University of Chicago Library':
        library = None

    if view == 'department' and query:
        sort = 'alphabetical'

    department_label = ''
    if department:
        department_label = department.split(' - ').pop()

    # staff pages
    staff_pages_all = []
    staff_pages = []

    if view == 'staff':
        # returns all staff pages if library is None.
        # otherwise, returns staff pages for the given library.
        staff_pages_all = get_staff_pages_for_library(library)

        # departments.
        if department:
            staff_pages_all = get_staff_pages_for_unit(department, True, True)

        # search staff pages.
        if query:
            staff_pages_all = staff_pages_all.search(query)

        # subjects.
        if subject:
            if subject == 'All Subject Specialists':
                staff_pages_all = staff_pages_all.filter(id__in=StaffPageSubjectPlacement.objects.all().values_list('page', flat=True).distinct())
            else:
                # get a subject and all it's descendants. 
                subject_and_descendants = Subject.objects.get(name=subject).get_descendants()
                # from staff page subject placements, get all of the staff that match those subjects. 
                subject_staff_ids = StaffPageSubjectPlacement.objects.filter(subject__in=subject_and_descendants).values_list('page', flat=True)
                # filter staff_pages_all to only include those staff pages. 
                staff_pages_all = staff_pages_all.filter(id__in=subject_staff_ids).order_by('last_name')

        # add paging.
        paginator = Paginator(staff_pages_all, 100)
        try:
            staff_pages = paginator.page(page)
        except PageNotAnInteger:
            staff_pages = paginator.page(1)
        except EmptyPage:
            staff_pages = paginator.page(paginator.num_pages)

    elif view == 'department':
        hierarchical_html = ''

        if query:
            units = UnitPage.objects.filter(display_in_directory=True).search(query)
            h = []
            for u in units:
                h.append(get_unit_info(Tree(u.title, u)))
            hierarchical_html = ''.join(h)
        else:
            hierarchical_html = get_html(UnitPage.hierarchical_units())
            # replace first ul. 
            if len(hierarchical_html) > 4:
                hierarchical_html = "<ul class='directory'>" + hierarchical_html[4:]
    
    default_image = Image.objects.get(title="Default Placeholder Photo")

    # Page context variables for templates
    home_page = StandardPage.objects.live().get(id=PUBLIC_HOMEPAGE)
    location_and_hours = get_hours_and_location(home_page)
    location = str(location_and_hours['page_location'])
    unit = location_and_hours['page_unit']

    return render(request, 'units/unit_index_page.html', {
        'breadcrumb_div_css': 'col-md-12 breadcrumbs hidden-xs hidden-sm',
        'content_div_css': 'container body-container col-xs-12 col-lg-11 col-lg-offset-1',
        'department': department,
        'department_label': department_label,
        'default_image': default_image,
        'hierarchical_units': hierarchical_html,
        'libraries': [str(p) for p in LocationPage.objects.live().filter(is_building=True)],
        'library': library,
        'query': query,
        'sort': sort,
        'staff_pages': staff_pages,
        'subjects': get_subjects(),
        'subject': subject,
        'view': view,
        'self': {
            'title': 'Library Directory'
        },
        'page_unit': str(unit),
        'page_location': location,
        'address': location_and_hours['address'],
        'chat_url': get_unit_chat_link(unit, request),
        'chat_status': get_chat_status('uofc-ask'),
        'chat_status_css': get_chat_status_css('uofc-ask'),
        'hours_page_url': home_page.get_hours_page(request),
        'quick_nums': get_quick_nums_for_library_or_dept(request),
    })
