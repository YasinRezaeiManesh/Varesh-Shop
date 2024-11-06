function sendProductComment(productId) {
    var comment = $('#commentText').val();
    var parentId = $('#parent_id').val()
    $.get('product-comment/', {
        productComment: comment,
        product_id: productId,
        parent_id: parentId,
    }).then(res => {
        $('#comment_area').html(res);
        $('#commentText').val('');
        $('#parent_id').val('');
    });
}


function fillParentId(parentId) {
    $('#parent_id').val(parentId);
    document.getElementById('scroll_me').scrollIntoView({behavior: "smooth"});
}


function sendArticleComment(articleId) {
    var comment = $('#commentTextArticle').val()
    var parentId = $('#parentIdArticle').val()
    $.get('add-article-comment/', {
        articleComment: comment,
        article_id: articleId,
        parent_id: parentId,
    }).then(res => {
        $('#comment_area_article').html(res);
        $('#commentTextArticle').val('');
        $('#parentIdArticle').val('');
    });
}


function fillParentIdArticle(parentIdArticle) {
    $('#parentIdArticle').val(parentIdArticle);
    document.getElementById('scroll_me').scrollIntoView({behavior: "smooth"});
}


function addProductToOrder(productId) {
    const productCount = $("#product-count").val();
    $.get("/order/add-to-order?product_id=" + productId + '&count=' + productCount).then(res => {
        Swal.fire({
            title: res.title,
            text: res.text,
            icon: res.icon,
            showCancelButton: false,
            confirmButtonColor: "#3085d6",
            confirmButtonText: res.confirm_button_text,
        }).then((result) => {
            if (result.isConfirmed && res.status === "user is not authenticated") {
                window.location.href = "/login";
            }
        });
    });
}

function removeOrderDetail(detailId){
    $.get("/user-panel/remove-order-detail?detail_id=" + detailId).then(res => {
        if (res.status === 'success') {
            $("#order-detail-content").html(res.body);
        }
    })
}


function changeOrderDetailCount(detailId, state){
    $.get("/user-panel/change-order-detail-count?detail_id=" + detailId + "&state=" + state).then(res => {
        if (res.status === 'success') {
            $("#order-detail-content").html(res.body);
        }
    })
}
