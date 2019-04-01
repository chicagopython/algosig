# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554091807.104521
_enable_loop = True
_template_filename = 'themes/custom/templates/tag.tmpl'
_template_uri = 'tag.tmpl'
_source_encoding = 'utf-8'
_exports = ['extra_head', 'content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('feeds_translations', context._clean_inheritance_tokens(), templateuri='feeds_translations_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'feeds_translations')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'list_post.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, 'feeds_translations')._populate(_import_ns, ['*'])
        description = _import_ns.get('description', context.get('description', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        posts = _import_ns.get('posts', context.get('posts', UNDEFINED))
        title = _import_ns.get('title', context.get('title', UNDEFINED))
        tag = _import_ns.get('tag', context.get('tag', UNDEFINED))
        subcategories = _import_ns.get('subcategories', context.get('subcategories', UNDEFINED))
        date_format = _import_ns.get('date_format', context.get('date_format', UNDEFINED))
        feeds_translations = _mako_get_namespace(context, 'feeds_translations')
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer('\n\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'feeds_translations')._populate(_import_ns, ['*'])
        feeds_translations = _mako_get_namespace(context, 'feeds_translations')
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        def extra_head():
            return render_extra_head(context)
        tag = _import_ns.get('tag', context.get('tag', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n    ')
        __M_writer(str(parent.extra_head()))
        __M_writer('\n    ')
        __M_writer(str(feeds_translations.head(tag)))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'feeds_translations')._populate(_import_ns, ['*'])
        description = _import_ns.get('description', context.get('description', UNDEFINED))
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        posts = _import_ns.get('posts', context.get('posts', UNDEFINED))
        title = _import_ns.get('title', context.get('title', UNDEFINED))
        tag = _import_ns.get('tag', context.get('tag', UNDEFINED))
        subcategories = _import_ns.get('subcategories', context.get('subcategories', UNDEFINED))
        date_format = _import_ns.get('date_format', context.get('date_format', UNDEFINED))
        feeds_translations = _mako_get_namespace(context, 'feeds_translations')
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n<article class="tagpage">\n    <header>\n        <div class="metadata">\n            ')
        __M_writer(str(feeds_translations.feed_link(tag)))
        __M_writer('\n        </div>\n        <h1>')
        __M_writer(filters.html_escape(str(title)))
        __M_writer('</h1>\n')
        if description:
            __M_writer('            <p>')
            __M_writer(str(description))
            __M_writer('</p>\n')
        if subcategories:
            __M_writer('        ')
            __M_writer(str(messages('Subcategories:')))
            __M_writer('\n        <ul>\n')
            for name, link in subcategories:
                __M_writer('            <li><a href="')
                __M_writer(str(link))
                __M_writer('">')
                __M_writer(filters.html_escape(str(name)))
                __M_writer('</a></li>\n')
            __M_writer('        </ul>\n')
        __M_writer('        ')
        __M_writer(str(feeds_translations.translation_link()))
        __M_writer('\n    </header>\n')
        if posts:
            __M_writer('        <ul class="postlist">\n')
            for post in posts:
                __M_writer('            <li itemscope itemtype="https://schema.org/BlogPosting">\n              <div><time class="metadata" datetime="')
                __M_writer(str(post.formatted_date('webiso')))
                __M_writer('" itemprop="datePublished">')
                __M_writer(filters.html_escape(str(post.formatted_date(date_format))))
                __M_writer('</time></div>\n              <div><a href="')
                __M_writer(str(post.permalink()))
                __M_writer('" itemprop="url">')
                __M_writer(filters.html_escape(str(post.title())))
                __M_writer('<a></div>\n            </li>\n')
            __M_writer('        </ul>\n')
        __M_writer('</article>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/custom/templates/tag.tmpl", "uri": "tag.tmpl", "source_encoding": "utf-8", "line_map": {"23": 3, "29": 0, "49": 2, "50": 3, "55": 8, "60": 42, "66": 5, "77": 5, "78": 6, "79": 6, "80": 7, "81": 7, "87": 11, "103": 11, "104": 15, "105": 15, "106": 17, "107": 17, "108": 18, "109": 19, "110": 19, "111": 19, "112": 21, "113": 22, "114": 22, "115": 22, "116": 24, "117": 25, "118": 25, "119": 25, "120": 25, "121": 25, "122": 27, "123": 29, "124": 29, "125": 29, "126": 31, "127": 32, "128": 33, "129": 34, "130": 35, "131": 35, "132": 35, "133": 35, "134": 36, "135": 36, "136": 36, "137": 36, "138": 39, "139": 41, "145": 139}}
__M_END_METADATA
"""
