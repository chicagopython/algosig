    

function ShowComments(repo_name, issue_id) {

    var url = "https://github.com/" + repo_name + "/issues/" + issue_id
    var api_url = "https://api.github.com/repos/" + repo_name + "/issues/" + issue_id + "/comments"
    
    $.ajax(api_url, {
        headers: {Accept: "application/vnd.github.v3.html+json"},
        dataType: "json",
        success: function(comments) {
            $("#gh-comments-list").append("Visit the <b><a href='" + url + "'>Github Issue</a></b> to comment on this post");
            $.each(comments, function(i, comment) {

                var date = new Date(comment.created_at);

                var t = "<li class='media my-4'>";
                //t += "<img src='" + comment.user.avatar_url + "' width='24px'>";
                t += "<img class='mr-3' src='" + comment.user.avatar_url + "'width='64px' alt='Generic placeholder image'>";
                t += "<div class='media-body'>";
                //t += "<b><a href='" + comment.user.html_url + "'>" + comment.user.login + "</a></b>";
                t += "<h5 class='mt-0 mb-1'>"+comment.user.login 
                t += "<small><i> "+ date.toUTCString() + "</i></small>"
                t += "</h5>"
                t += comment.body_html;
                t += "</div>";
                t += "</li>";
                $("#gh-comments-list").append(t);
            });
        },
        error: function() {
            $("#gh-comments-list").append("Comments are not open for this post yet.");
        }
    });
}