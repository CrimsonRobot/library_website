from django import template
from public.models import LocationPage, StaffPublicPage
from staff.models import StaffPage

register = template.Library()

@register.filter
def ofKey(value, arg):
    if value:
        return value.get(arg)
    else:
        return ''

@register.inclusion_tag('units/library_unit_links.html')
def library_unit_links(library_unit):
    try:
        library_unit_pieces = library_unit.get_full_name().split(' - ')
    except AttributeError:
        return {
            'units': []
        }
    units = []
    i = 0
    while i < len(library_unit_pieces):
        link_param = ' - '.join(library_unit_pieces[:i+1])
        link_text = library_unit_pieces[i]
        units.append([
            link_param,
            link_text
        ])
        i = i + 1
    return {
        'units': units
    }

@register.inclusion_tag('units/staff_email_addresses.html')
def staff_email_addresses(staff_page):
    return {
        'emails': list(set(staff_page.staff_page_email.all().values_list('email', flat=True)))
    }

@register.inclusion_tag('units/staff_faculty_exchanges_phone_numbers.html')
def staff_faculty_exchanges_phone_numbers(staff_page):
    facex_phone_pairs = set()
    for p in staff_page.staff_page_phone_faculty_exchange.all():
        facex_phone_pairs.add(p.faculty_exchange + '\t' + p.phone_number)
    
    facex_phone_pairs_list = list(map(lambda p: p.split('\t'), list(facex_phone_pairs)))

    lib_room_phone = []
    for p in facex_phone_pairs_list:
        facex_parts = p[0].split(' ')
       
        lib = '' 
        if facex_parts[0] == 'JCL':     
            lib = LocationPage.objects.get(title='The John Crerar Library')
        elif facex_parts[0] == 'JRL':
            lib = LocationPage.objects.get(title='The Joseph Regenstein Library')
        elif facex_parts[0] == 'LBQ':
            lib = LocationPage.objects.get(title='The D\'Angelo Law Library')
        elif facex_parts[0] in ['MAN', 'Mansueto']:
            lib = LocationPage.objects.get(title='The Joe and Rika Mansueto Library')
        elif facex_parts[0] == 'SSA':
            lib = LocationPage.objects.get(title='Social Service Administration Library')
        else:
            lib = None

        if len(facex_parts) > 1:
            room = facex_parts[1]
        else:
            room = None

        if p[1]:
            phone = p[1]
        else:
            phone = None
       
        lib_room_phone.append([lib, room, phone])
    
    return {
        'lib_room_phone': lib_room_phone
    }
    
@register.inclusion_tag('units/staff_subjects.html')
def staff_subjects(staff_page):
    subjects = []
    for s in staff_page.staff_subject_placements.all():
        subjects.append(s.subject.name)
    
    return {
        'subjects': sorted(subjects)
    }

@register.inclusion_tag('units/staff_public_page_link.html')
def staff_public_page_link(staff_page):
    
    try:
        href = StaffPublicPage.objects.get(cnetid=staff_page.cnetid).url
    except:
        href = ''
       
    return {
        'href': href,
        'title': staff_page.title
    }
    
