# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554091383.999899
_enable_loop = True
_template_filename = 'themes/custom/templates/comments_helper.tmpl'
_template_uri = 'comments_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['comment_form', 'comment_link', 'comment_link_script']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('disqus', context._clean_inheritance_tokens(), templateuri='comments_helper_disqus.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'disqus')] = ns

    ns = runtime.TemplateNamespace('intensedebate', context._clean_inheritance_tokens(), templateuri='comments_helper_intensedebate.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'intensedebate')] = ns

    ns = runtime.TemplateNamespace('muut', context._clean_inheritance_tokens(), templateuri='comments_helper_muut.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'muut')] = ns

    ns = runtime.TemplateNamespace('facebook', context._clean_inheritance_tokens(), templateuri='comments_helper_facebook.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'facebook')] = ns

    ns = runtime.TemplateNamespace('isso', context._clean_inheritance_tokens(), templateuri='comments_helper_isso.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'isso')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_form(context,url,title,identifier):
    __M_caller = context.caller_stack._push_frame()
    try:
        muut = _mako_get_namespace(context, 'muut')
        disqus = _mako_get_namespace(context, 'disqus')
        livefyre = context.get('livefyre', UNDEFINED)
        comment_system = context.get('comment_system', UNDEFINED)
        intensedebate = _mako_get_namespace(context, 'intensedebate')
        facebook = _mako_get_namespace(context, 'facebook')
        isso = _mako_get_namespace(context, 'isso')
        googleplus = context.get('googleplus', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if comment_system == 'disqus':
            __M_writer('        ')
            __M_writer(str(disqus.comment_form(url, title, identifier)))
            __M_writer('\n')
        elif comment_system == 'livefyre':
            __M_writer('        ')
            __M_writer(str(livefyre.comment_form(url, title, identifier)))
            __M_writer('\n')
        elif comment_system == 'intensedebate':
            __M_writer('        ')
            __M_writer(str(intensedebate.comment_form(url, title, identifier)))
            __M_writer('\n')
        elif comment_system == 'muut':
            __M_writer('        ')
            __M_writer(str(muut.comment_form(url, title, identifier)))
            __M_writer('\n')
        elif comment_system == 'googleplus':
            __M_writer('        ')
            __M_writer(str(googleplus.comment_form(url, title, identifier)))
            __M_writer('\n')
        elif comment_system == 'facebook':
            __M_writer('        ')
            __M_writer(str(facebook.comment_form(url, title, identifier)))
            __M_writer('\n')
        elif comment_system == 'isso':
            __M_writer('        ')
            __M_writer(str(isso.comment_form(url, title, identifier)))
            __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_link(context,link,identifier):
    __M_caller = context.caller_stack._push_frame()
    try:
        muut = _mako_get_namespace(context, 'muut')
        disqus = _mako_get_namespace(context, 'disqus')
        livefyre = context.get('livefyre', UNDEFINED)
        comment_system = context.get('comment_system', UNDEFINED)
        intensedebate = _mako_get_namespace(context, 'intensedebate')
        facebook = _mako_get_namespace(context, 'facebook')
        isso = _mako_get_namespace(context, 'isso')
        googleplus = context.get('googleplus', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if comment_system == 'disqus':
            __M_writer('        ')
            __M_writer(str(disqus.comment_link(link, identifier)))
            __M_writer('\n')
        elif comment_system == 'livefyre':
            __M_writer('        ')
            __M_writer(str(livefyre.comment_link(link, identifier)))
            __M_writer('\n')
        elif comment_system == 'intensedebate':
            __M_writer('        ')
            __M_writer(str(intensedebate.comment_link(link, identifier)))
            __M_writer('\n')
        elif comment_system == 'muut':
            __M_writer('        ')
            __M_writer(str(muut.comment_link(link, identifier)))
            __M_writer('\n')
        elif comment_system == 'googleplus':
            __M_writer('        ')
            __M_writer(str(googleplus.comment_link(link, identifier)))
            __M_writer('\n')
        elif comment_system == 'facebook':
            __M_writer('        ')
            __M_writer(str(facebook.comment_link(link, identifier)))
            __M_writer('\n')
        elif comment_system == 'isso':
            __M_writer('        ')
            __M_writer(str(isso.comment_link(link, identifier)))
            __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_link_script(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        muut = _mako_get_namespace(context, 'muut')
        disqus = _mako_get_namespace(context, 'disqus')
        livefyre = context.get('livefyre', UNDEFINED)
        comment_system = context.get('comment_system', UNDEFINED)
        intensedebate = _mako_get_namespace(context, 'intensedebate')
        facebook = _mako_get_namespace(context, 'facebook')
        isso = _mako_get_namespace(context, 'isso')
        googleplus = context.get('googleplus', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if comment_system == 'disqus':
            __M_writer('        ')
            __M_writer(str(disqus.comment_link_script()))
            __M_writer('\n')
        elif comment_system == 'livefyre':
            __M_writer('        ')
            __M_writer(str(livefyre.comment_link_script()))
            __M_writer('\n')
        elif comment_system == 'intensedebate':
            __M_writer('        ')
            __M_writer(str(intensedebate.comment_link_script()))
            __M_writer('\n')
        elif comment_system == 'muut':
            __M_writer('        ')
            __M_writer(str(muut.comment_link_script()))
            __M_writer('\n')
        elif comment_system == 'googleplus':
            __M_writer('        ')
            __M_writer(str(googleplus.comment_link_script()))
            __M_writer('\n')
        elif comment_system == 'facebook':
            __M_writer('        ')
            __M_writer(str(facebook.comment_link_script()))
            __M_writer('\n')
        elif comment_system == 'isso':
            __M_writer('        ')
            __M_writer(str(isso.comment_link_script()))
            __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/custom/templates/comments_helper.tmpl", "uri": "comments_helper.tmpl", "source_encoding": "utf-8", "line_map": {"23": 3, "26": 4, "29": 5, "32": 6, "35": 7, "38": 0, "43": 2, "44": 3, "45": 4, "46": 5, "47": 6, "48": 7, "49": 25, "50": 43, "51": 61, "57": 9, "69": 9, "70": 10, "71": 11, "72": 11, "73": 11, "74": 12, "75": 13, "76": 13, "77": 13, "78": 14, "79": 15, "80": 15, "81": 15, "82": 16, "83": 17, "84": 17, "85": 17, "86": 18, "87": 19, "88": 19, "89": 19, "90": 20, "91": 21, "92": 21, "93": 21, "94": 22, "95": 23, "96": 23, "97": 23, "103": 27, "115": 27, "116": 28, "117": 29, "118": 29, "119": 29, "120": 30, "121": 31, "122": 31, "123": 31, "124": 32, "125": 33, "126": 33, "127": 33, "128": 34, "129": 35, "130": 35, "131": 35, "132": 36, "133": 37, "134": 37, "135": 37, "136": 38, "137": 39, "138": 39, "139": 39, "140": 40, "141": 41, "142": 41, "143": 41, "149": 45, "161": 45, "162": 46, "163": 47, "164": 47, "165": 47, "166": 48, "167": 49, "168": 49, "169": 49, "170": 50, "171": 51, "172": 51, "173": 51, "174": 52, "175": 53, "176": 53, "177": 53, "178": 54, "179": 55, "180": 55, "181": 55, "182": 56, "183": 57, "184": 57, "185": 57, "186": 58, "187": 59, "188": 59, "189": 59, "195": 189}}
__M_END_METADATA
"""
