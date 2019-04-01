# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554091134.526242
_enable_loop = True
_template_filename = 'themes/custom/templates/post_helper.tmpl'
_template_uri = 'post_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['meta_translations', 'html_tags', 'html_pager', 'open_graph_metadata', 'twitter_card_information']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('math', context._clean_inheritance_tokens(), templateuri='math_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'math')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_meta_translations(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        len = context.get('len', UNDEFINED)
        sorted = context.get('sorted', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if len(translations) > 1:
            for langname in sorted(translations):
                if langname != lang and ((not post.skip_untranslated) or post.is_translation_available(langname)):
                    __M_writer('                <link rel="alternate" hreflang="')
                    __M_writer(str(langname))
                    __M_writer('" href="')
                    __M_writer(str(post.permalink(langname)))
                    __M_writer('">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_tags(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        _link = context.get('_link', UNDEFINED)
        hidden_tags = context.get('hidden_tags', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if post.tags or post.meta('category'):
            __M_writer('      <ul itemprop="keywords" class="tags">\n')
            if post.meta('category'):
                __M_writer('          <li><a class="tag p-category" href="')
                __M_writer(str(_link('category', post.meta('category').lower())))
                __M_writer('" rel="category"> ')
                __M_writer(filters.html_escape(str(post.meta('category'))))
                __M_writer('</a></li>\n')
            for tag in post.tags:
                if tag not in hidden_tags:
                    __M_writer('            <li><a class="tag p-category" href="')
                    __M_writer(str(_link('tag', tag)))
                    __M_writer('" rel="tag">')
                    __M_writer(filters.html_escape(str(tag)))
                    __M_writer('</a></li>\n')
            __M_writer('      </ul>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_pager(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        messages = context.get('messages', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    <ul class="pager hidden-print">\n        <li>\n')
        if post.prev_post:
            __M_writer('            <a href="')
            __M_writer(str(post.prev_post.permalink()))
            __M_writer('" rel="prev" class="previous" title="')
            __M_writer(filters.html_escape(str(post.prev_post.title())))
            __M_writer('"><span aria-hidden="true">‹ </span>')
            __M_writer(str(messages("Older")))
            __M_writer('</a>\n')
        else:
            __M_writer('            <span class="disabled"><span aria-hidden="true">‹ </span>')
            __M_writer(str(messages("Older")))
            __M_writer('</span>\n')
        __M_writer('        </li>\n        <li>\n')
        if post.next_post:
            __M_writer('            <a href="')
            __M_writer(str(post.next_post.permalink()))
            __M_writer('" rel="next" class="next" title="')
            __M_writer(filters.html_escape(str(post.next_post.title())))
            __M_writer('">')
            __M_writer(str(messages("Newer")))
            __M_writer('<span aria-hidden="true"> ›</span></a>\n')
        else:
            __M_writer('            <span class="disabled">')
            __M_writer(str(messages("Newer")))
            __M_writer('<span aria-hidden="true"> ›</span></span>\n')
        __M_writer('        </li>\n    </ul>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_open_graph_metadata(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        blog_title = context.get('blog_title', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        use_open_graph = context.get('use_open_graph', UNDEFINED)
        abs_link = context.get('abs_link', UNDEFINED)
        permalink = context.get('permalink', UNDEFINED)
        url_replacer = context.get('url_replacer', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if use_open_graph:
            __M_writer('    <meta property="og:site_name" content="')
            __M_writer(filters.html_escape(str(blog_title)))
            __M_writer('">\n    <meta property="og:title" content="')
            __M_writer(filters.html_escape(str(post.title()[:70])))
            __M_writer('">\n    <meta property="og:url" content="')
            __M_writer(str(abs_link(permalink)))
            __M_writer('">\n')
            if post.description():
                __M_writer('    <meta property="og:description" content="')
                __M_writer(filters.html_escape(str(post.description()[:200])))
                __M_writer('">\n')
            else:
                __M_writer('    <meta property="og:description" content="')
                __M_writer(filters.html_escape(str(post.text(strip_html=True)[:200])))
                __M_writer('">\n')
            if post.previewimage:
                __M_writer('    <meta property="og:image" content="')
                __M_writer(str(url_replacer(permalink, post.previewimage, lang, 'absolute')))
                __M_writer('">\n')
            __M_writer('    <meta property="og:type" content="article">\n')
            if post.date.isoformat():
                __M_writer('    <meta property="article:published_time" content="')
                __M_writer(str(post.formatted_date('webiso')))
                __M_writer('">\n')
            if post.tags:
                for tag in post.tags:
                    __M_writer('           <meta property="article:tag" content="')
                    __M_writer(filters.html_escape(str(tag)))
                    __M_writer('">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_twitter_card_information(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        twitter_card = context.get('twitter_card', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if twitter_card and twitter_card['use_twitter_cards']:
            __M_writer('    <meta name="twitter:card" content="')
            __M_writer(filters.html_escape(str(twitter_card.get('card', 'summary'))))
            __M_writer('">\n')
            if 'site:id' in twitter_card:
                __M_writer('    <meta name="twitter:site:id" content="')
                __M_writer(str(twitter_card['site:id']))
                __M_writer('">\n')
            elif 'site' in twitter_card:
                __M_writer('    <meta name="twitter:site" content="')
                __M_writer(str(twitter_card['site']))
                __M_writer('">\n')
            if 'creator:id' in twitter_card:
                __M_writer('    <meta name="twitter:creator:id" content="')
                __M_writer(str(twitter_card['creator:id']))
                __M_writer('">\n')
            elif 'creator' in twitter_card:
                __M_writer('    <meta name="twitter:creator" content="')
                __M_writer(str(twitter_card['creator']))
                __M_writer('">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/custom/templates/post_helper.tmpl", "uri": "post_helper.tmpl", "source_encoding": "utf-8", "line_map": {"23": 2, "26": 0, "31": 2, "32": 12, "33": 27, "34": 46, "35": 75, "36": 91, "42": 4, "50": 4, "51": 5, "52": 6, "53": 7, "54": 8, "55": 8, "56": 8, "57": 8, "58": 8, "64": 14, "70": 14, "71": 15, "72": 16, "73": 17, "74": 18, "75": 18, "76": 18, "77": 18, "78": 18, "79": 20, "80": 21, "81": 22, "82": 22, "83": 22, "84": 22, "85": 22, "86": 25, "92": 29, "97": 29, "98": 32, "99": 33, "100": 33, "101": 33, "102": 33, "103": 33, "104": 33, "105": 33, "106": 34, "107": 35, "108": 35, "109": 35, "110": 37, "111": 39, "112": 40, "113": 40, "114": 40, "115": 40, "116": 40, "117": 40, "118": 40, "119": 41, "120": 42, "121": 42, "122": 42, "123": 44, "129": 48, "139": 48, "140": 49, "141": 50, "142": 50, "143": 50, "144": 51, "145": 51, "146": 52, "147": 52, "148": 53, "149": 54, "150": 54, "151": 54, "152": 55, "153": 56, "154": 56, "155": 56, "156": 58, "157": 59, "158": 59, "159": 59, "160": 61, "161": 66, "162": 67, "163": 67, "164": 67, "165": 69, "166": 70, "167": 71, "168": 71, "169": 71, "175": 77, "180": 77, "181": 78, "182": 79, "183": 79, "184": 79, "185": 80, "186": 81, "187": 81, "188": 81, "189": 82, "190": 83, "191": 83, "192": 83, "193": 85, "194": 86, "195": 86, "196": 86, "197": 87, "198": 88, "199": 88, "200": 88, "206": 200}}
__M_END_METADATA
"""
