# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554091636.855732
_enable_loop = True
_template_filename = 'themes/custom/templates/base_header.tmpl'
_template_uri = 'base_header.tmpl'
_source_encoding = 'utf-8'
_exports = ['html_header', 'html_site_title', 'html_navigation_links', 'html_translation_header']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('base', context._clean_inheritance_tokens(), templateuri='base_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'base')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        __M_writer = context.writer()
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_header(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        def html_navigation_links():
            return render_html_navigation_links(context)
        template_hooks = _import_ns.get('template_hooks', context.get('template_hooks', UNDEFINED))
        def html_translation_header():
            return render_html_translation_header(context)
        search_form = _import_ns.get('search_form', context.get('search_form', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n    <header id="header" class="hidden-print">\n        ')
        __M_writer(str(html_translation_header()))
        __M_writer('\n        ')
        __M_writer(str(html_navigation_links()))
        __M_writer('\n')
        if search_form:
            __M_writer('            <div class="searchform" role="search">\n                ')
            __M_writer(str(search_form))
            __M_writer('\n            </div>\n')
        __M_writer('    </header>\n    ')
        __M_writer(str(template_hooks['page_header']()))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_site_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        _link = _import_ns.get('_link', context.get('_link', UNDEFINED))
        show_blog_title = _import_ns.get('show_blog_title', context.get('show_blog_title', UNDEFINED))
        logo_url = _import_ns.get('logo_url', context.get('logo_url', UNDEFINED))
        blog_title = _import_ns.get('blog_title', context.get('blog_title', UNDEFINED))
        abs_link = _import_ns.get('abs_link', context.get('abs_link', UNDEFINED))
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n    <a href="')
        __M_writer(str(abs_link(_link("root", None, lang))))
        __M_writer('" title="')
        __M_writer(filters.html_escape(str(blog_title)))
        __M_writer('" rel="home">\n')
        if logo_url:
            __M_writer('        <img src="')
            __M_writer(str(logo_url))
            __M_writer('" alt="')
            __M_writer(filters.html_escape(str(blog_title)))
            __M_writer('" id="logo" \n')
        __M_writer('\n')
        if show_blog_title:
            __M_writer('      aria-hidden>\n          ')
            __M_writer(filters.html_escape(str(blog_title)))
            __M_writer('\n')
        else:
            if logo_url:
                __M_writer('        >\n')
        __M_writer('    </a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_navigation_links(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        isinstance = _import_ns.get('isinstance', context.get('isinstance', UNDEFINED))
        rel_link = _import_ns.get('rel_link', context.get('rel_link', UNDEFINED))
        navigation_links = _import_ns.get('navigation_links', context.get('navigation_links', UNDEFINED))
        template_hooks = _import_ns.get('template_hooks', context.get('template_hooks', UNDEFINED))
        show_blog_title = _import_ns.get('show_blog_title', context.get('show_blog_title', UNDEFINED))
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        permalink = _import_ns.get('permalink', context.get('permalink', UNDEFINED))
        tuple = _import_ns.get('tuple', context.get('tuple', UNDEFINED))
        def html_site_title():
            return render_html_site_title(context)
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n    <nav id="menu">\n')
        if show_blog_title:
            __M_writer('    ')
            __M_writer(str(html_site_title()))
            __M_writer('\n')
        __M_writer('    <ul>\n')
        for url, text in navigation_links[lang]:
            if isinstance(url, tuple):
                __M_writer('            <li> ')
                __M_writer(str(text))
                __M_writer('\n')
                for suburl, text in url:
                    if rel_link(permalink, suburl) == "#":
                        __M_writer('                    <li class="active"><a href="')
                        __M_writer(str(permalink))
                        __M_writer('">')
                        __M_writer(str(text))
                        __M_writer('<span class="sr-only"> ')
                        __M_writer(str(messages("(active)", lang)))
                        __M_writer('</span></a></li>\n')
                    else:
                        __M_writer('                    <li><a href="')
                        __M_writer(str(suburl))
                        __M_writer('">')
                        __M_writer(str(text))
                        __M_writer('</a></li>\n')
            else:
                if rel_link(permalink, url) == "#":
                    __M_writer('                <li class="active"><a href="')
                    __M_writer(str(permalink))
                    __M_writer('">')
                    __M_writer(str(text))
                    __M_writer('<span class="sr-only"> ')
                    __M_writer(str(messages("(active)", lang)))
                    __M_writer('</span></a></li>\n')
                else:
                    __M_writer('                <li><a href="')
                    __M_writer(str(url))
                    __M_writer('">')
                    __M_writer(str(text))
                    __M_writer('</a></li>\n')
        __M_writer('    ')
        __M_writer(str(template_hooks['menu']()))
        __M_writer('\n    ')
        __M_writer(str(template_hooks['menu_alt']()))
        __M_writer('\n    </ul>\n    </nav>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_translation_header(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        base = _mako_get_namespace(context, 'base')
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        translations = _import_ns.get('translations', context.get('translations', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n')
        if len(translations) > 1:
            __M_writer('        <div id="toptranslations">\n            <h2>')
            __M_writer(str(messages("Languages:")))
            __M_writer('</h2>\n            ')
            __M_writer(str(base.html_translations()))
            __M_writer('\n        </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/custom/templates/base_header.tmpl", "uri": "base_header.tmpl", "source_encoding": "utf-8", "line_map": {"23": 2, "26": 0, "33": 2, "34": 15, "35": 32, "36": 62, "37": 71, "43": 4, "55": 4, "56": 6, "57": 6, "58": 7, "59": 7, "60": 8, "61": 9, "62": 10, "63": 10, "64": 13, "65": 14, "66": 14, "72": 17, "84": 17, "85": 18, "86": 18, "87": 18, "88": 18, "89": 19, "90": 20, "91": 20, "92": 20, "93": 20, "94": 20, "95": 22, "96": 23, "97": 24, "98": 25, "99": 25, "100": 26, "101": 27, "102": 28, "103": 31, "109": 34, "126": 34, "127": 36, "128": 37, "129": 37, "130": 37, "131": 39, "132": 40, "133": 41, "134": 42, "135": 42, "136": 42, "137": 43, "138": 44, "139": 45, "140": 45, "141": 45, "142": 45, "143": 45, "144": 45, "145": 45, "146": 46, "147": 47, "148": 47, "149": 47, "150": 47, "151": 47, "152": 50, "153": 51, "154": 52, "155": 52, "156": 52, "157": 52, "158": 52, "159": 52, "160": 52, "161": 53, "162": 54, "163": 54, "164": 54, "165": 54, "166": 54, "167": 58, "168": 58, "169": 58, "170": 59, "171": 59, "177": 64, "187": 64, "188": 65, "189": 66, "190": 67, "191": 67, "192": 68, "193": 68, "199": 193}}
__M_END_METADATA
"""
