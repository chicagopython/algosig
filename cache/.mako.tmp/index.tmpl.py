# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554091721.501801
_enable_loop = True
_template_filename = 'themes/custom/templates/index.tmpl'
_template_uri = 'index.tmpl'
_source_encoding = 'utf-8'
_exports = ['extra_head', 'content', 'content_header']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('helper', context._clean_inheritance_tokens(), templateuri='index_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'helper')] = ns

    ns = runtime.TemplateNamespace('post_helper', context._clean_inheritance_tokens(), templateuri='post_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'post_helper')] = ns

    ns = runtime.TemplateNamespace('math', context._clean_inheritance_tokens(), templateuri='math_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'math')] = ns

    ns = runtime.TemplateNamespace('require', context._clean_inheritance_tokens(), templateuri='require_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'require')] = ns

    ns = runtime.TemplateNamespace('comments', context._clean_inheritance_tokens(), templateuri='comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'comments')] = ns

    ns = runtime.TemplateNamespace('pagination', context._clean_inheritance_tokens(), templateuri='pagination_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'pagination')] = ns

    ns = runtime.TemplateNamespace('feeds_translations', context._clean_inheritance_tokens(), templateuri='feeds_translations_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'feeds_translations')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, 'feeds_translations')._populate(_import_ns, ['*'])
        math = _mako_get_namespace(context, 'math')
        def content_header():
            return render_content_header(context._locals(__M_locals))
        prev_next_links_reversed = _import_ns.get('prev_next_links_reversed', context.get('prev_next_links_reversed', UNDEFINED))
        comments = _mako_get_namespace(context, 'comments')
        prevlink = _import_ns.get('prevlink', context.get('prevlink', UNDEFINED))
        permalink = _import_ns.get('permalink', context.get('permalink', UNDEFINED))
        index_teasers = _import_ns.get('index_teasers', context.get('index_teasers', UNDEFINED))
        nextlink = _import_ns.get('nextlink', context.get('nextlink', UNDEFINED))
        date_format = _import_ns.get('date_format', context.get('date_format', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        post_helper = _mako_get_namespace(context, 'post_helper')
        current_page = _import_ns.get('current_page', context.get('current_page', UNDEFINED))
        require = _mako_get_namespace(context, 'require')
        front_index_header = _import_ns.get('front_index_header', context.get('front_index_header', UNDEFINED))
        page_links = _import_ns.get('page_links', context.get('page_links', UNDEFINED))
        feeds_translations = _mako_get_namespace(context, 'feeds_translations')
        pagekind = _import_ns.get('pagekind', context.get('pagekind', UNDEFINED))
        helper = _mako_get_namespace(context, 'helper')
        data = _import_ns.get('data', context.get('data', UNDEFINED))
        def content():
            return render_content(context._locals(__M_locals))
        index_file = _import_ns.get('index_file', context.get('index_file', UNDEFINED))
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        posts = _import_ns.get('posts', context.get('posts', UNDEFINED))
        pagination = _mako_get_namespace(context, 'pagination')
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer('\n\n')
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
        math = _mako_get_namespace(context, 'math')
        require = _mako_get_namespace(context, 'require')
        index_file = _import_ns.get('index_file', context.get('index_file', UNDEFINED))
        def extra_head():
            return render_extra_head(context)
        permalink = _import_ns.get('permalink', context.get('permalink', UNDEFINED))
        posts = _import_ns.get('posts', context.get('posts', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n    ')
        __M_writer(str(parent.extra_head()))
        if posts and (permalink == '/' or permalink == '/' + index_file):
            __M_writer('        <link rel="prefetch" href="')
            __M_writer(str(posts[0].permalink()))
            __M_writer('" type="text/html">\n')
        __M_writer('    ')
        __M_writer(str(math.math_styles_ifposts(posts)))
        __M_writer('    ')
        __M_writer(str(require.require_script_ifposts(posts)))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'feeds_translations')._populate(_import_ns, ['*'])
        prev_next_links_reversed = _import_ns.get('prev_next_links_reversed', context.get('prev_next_links_reversed', UNDEFINED))
        def content_header():
            return render_content_header(context)
        math = _mako_get_namespace(context, 'math')
        comments = _mako_get_namespace(context, 'comments')
        prevlink = _import_ns.get('prevlink', context.get('prevlink', UNDEFINED))
        index_teasers = _import_ns.get('index_teasers', context.get('index_teasers', UNDEFINED))
        nextlink = _import_ns.get('nextlink', context.get('nextlink', UNDEFINED))
        date_format = _import_ns.get('date_format', context.get('date_format', UNDEFINED))
        post_helper = _mako_get_namespace(context, 'post_helper')
        current_page = _import_ns.get('current_page', context.get('current_page', UNDEFINED))
        front_index_header = _import_ns.get('front_index_header', context.get('front_index_header', UNDEFINED))
        page_links = _import_ns.get('page_links', context.get('page_links', UNDEFINED))
        feeds_translations = _mako_get_namespace(context, 'feeds_translations')
        pagekind = _import_ns.get('pagekind', context.get('pagekind', UNDEFINED))
        helper = _mako_get_namespace(context, 'helper')
        data = _import_ns.get('data', context.get('data', UNDEFINED))
        def content():
            return render_content(context)
        posts = _import_ns.get('posts', context.get('posts', UNDEFINED))
        pagination = _mako_get_namespace(context, 'pagination')
        __M_writer = context.writer()
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_header'):
            context['self'].content_header(**pageargs)
        

        __M_writer('\n')
        if 'main_index' in pagekind:
            __M_writer('    ')
            __M_writer(str(front_index_header))
        if page_links:
            __M_writer('    ')
            __M_writer(str(pagination.page_navigation(current_page, page_links, prevlink, nextlink, prev_next_links_reversed)))
        __M_writer('<div class="postindex">\n')
        for post in posts:
            __M_writer('    <article class="h-entry post-')
            __M_writer(str(post.meta('type')))
            __M_writer('">\n')
            if post.meta('previewimage'):
                __M_writer('      <img src="')
                __M_writer(str(post.meta('previewimage')))
                __M_writer('" alt="article thumbnail">\n')
            elif post.meta('category') in data['default_thumbnails']:
                __M_writer('      <img src="')
                __M_writer(str(data['default_thumbnails'][post.meta('category')]))
                __M_writer('" alt="article thumbnail">\n')
            else:
                __M_writer('      <img src="')
                __M_writer(str(data['default_thumbnails']['']))
                __M_writer('" alt="article thumbnail">\n')
            __M_writer('    <h3 class="p-name entry-title"><a href="')
            __M_writer(str(post.permalink()))
            __M_writer('" class="u-url">')
            __M_writer(filters.html_escape(str(post.title())))
            __M_writer('</a></h3>\n    <span class="metadata">\n        <time datetime="')
            __M_writer(str(post.formatted_date('webiso')))
            __M_writer('">')
            __M_writer(filters.html_escape(str(post.formatted_date(date_format))))
            __M_writer('</time>\n        <i class="fas fa-tags"></i>\n        ')
            __M_writer(str(post_helper.html_tags(post)))
            __M_writer('\n    </span>\n    <!--\n')
            if index_teasers:
                __M_writer('    <div class="p-summary entry-summary">\n    ')
                __M_writer(str(post.text(teaser_only=True)))
                __M_writer('    <hr/>\n')
            else:
                __M_writer('    <div class="e-content entry-content">\n    ')
                __M_writer(str(post.text(teaser_only=False)))
            __M_writer('    </div>-->\n    </article>\n')
        __M_writer('</div>\n')
        __M_writer(str(helper.html_pager()))
        __M_writer(str(comments.comment_link_script()))
        __M_writer(str(math.math_scripts_ifposts(posts)))
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_header(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'feeds_translations')._populate(_import_ns, ['*'])
        def content_header():
            return render_content_header(context)
        feeds_translations = _mako_get_namespace(context, 'feeds_translations')
        __M_writer = context.writer()
        __M_writer('\n    ')
        __M_writer(str(feeds_translations.translation_link()))
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/custom/templates/index.tmpl", "uri": "index.tmpl", "source_encoding": "utf-8", "line_map": {"23": 2, "26": 3, "29": 4, "32": 5, "35": 6, "38": 7, "41": 8, "47": 0, "81": 2, "82": 3, "83": 4, "84": 5, "85": 6, "86": 7, "87": 8, "88": 9, "93": 18, "98": 62, "104": 11, "118": 11, "119": 12, "120": 13, "121": 14, "122": 14, "123": 14, "124": 16, "125": 16, "126": 17, "127": 17, "128": 17, "134": 20, "161": 20, "166": 23, "167": 24, "168": 25, "169": 25, "170": 27, "171": 28, "172": 28, "173": 30, "174": 31, "175": 32, "176": 32, "177": 32, "178": 33, "179": 34, "180": 34, "181": 34, "182": 35, "183": 36, "184": 36, "185": 36, "186": 37, "187": 38, "188": 38, "189": 38, "190": 40, "191": 40, "192": 40, "193": 40, "194": 40, "195": 42, "196": 42, "197": 42, "198": 42, "199": 44, "200": 44, "201": 47, "202": 48, "203": 49, "204": 50, "205": 51, "206": 52, "207": 53, "208": 55, "209": 58, "210": 59, "211": 60, "212": 61, "218": 21, "227": 21, "228": 22, "234": 228}}
__M_END_METADATA
"""
