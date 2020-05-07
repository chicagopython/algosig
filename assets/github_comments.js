function ShowComments(repo_name, issue_id) {

    var api_url = "https://api.github.com/repos/" + repo_name + "/issues/" + issue_id + "/comments?page=1&per_page=100"

    $.ajax(api_url, {
        headers: {Accept: "application/vnd.github.v3.html+json"},
        dataType: "json",
        success: function(comments) {
            $.each(comments, function(i, comment) {

                var date = new Date(comment.created_at);
                const options = { year: 'numeric', month: 'long', day: 'numeric', hour: 'numeric', minute: 'numeric' }
                var f_date = date.toLocaleDateString(undefined, options);

                var t = `
                    <div class='media my-2'>
                        <div class='media-left mr-3'>
                            <img class='rounded media-object' src=' ${comment.user.avatar_url}' style='width:50px'>
                        </div>
                        <div class='media-body'>
                            <h5 class='media-heading'>
                                ${comment.user.login}
                                <small><i>${f_date}</i></small>
                            </h5>
                            ${comment.body_html}
                        </div>
                    </div>
                `;

                $("#gh-comments-list").append(t);
            });
        },
        error: function() {
            $("#gh-comments-list").append("Comments are not open for this post yet.");
        }
    });
}
