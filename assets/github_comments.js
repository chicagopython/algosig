    

function ShowComments(repo_name, issue_id) {

    var url = "https://github.com/" + repo_name + "/issues/" + issue_id
    var api_url = "https://api.github.com/repos/" + repo_name + "/issues/" + issue_id + "/comments?page=1&per_page=100"
    
    $.ajax(api_url, {
        headers: {Accept: "application/vnd.github.v3.html+json"},
        dataType: "json",
        success: function(comments) {
            $("#gh-comments-list").append("Visit the <b><a href='" + url + "'>Github Issue</a></b> to comment on this post");
            $.each(comments, function(i, comment) {

                var date = new Date(comment.created_at);

                var t = "<div class='media my-4'>";
                t += "<div class='media-left mr-3'><img class='media-object' src='" + comment.user.avatar_url + "'style='width:64px'>";
                t += "</div>";
                t += "<div class='media-body'>";
                //t += "<b><a href='" + comment.user.html_url + "'>" + comment.user.login + "</a></b>";
                t += "<h5 class='media-heading'> "+comment.user.login;
                var localDateString = date.toString();
                localDateString = localDateString.substring(0, localDateString.lastIndexOf(":"));
                t += "<small><i> "+ localDateString  + "</i></small>";
                t += "</h5>";
                t += comment.body_html;
                t += "</div>";
                t += "</div>";
                $("#gh-comments-list").append(t);
            });
        },
        error: function() {
            $("#gh-comments-list").append("Comments are not open for this post yet.");
        }
    });
}