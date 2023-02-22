from newspaper_app.models import Category, Tag, Post

from django.db.models import F, Sum, Case, When


def navigation(request):
    categories = Category.objects.all()
    tags = Tag.objects.all()[:10]
    # Get the post with the highest views_count of posts in each category
    top_categories = (
        Post.objects.values("category__pk", "category__name")
        .annotate(
            pk=F("category__pk"), name=F("category__name"), max_views=Sum("views_count")
        )
        .order_by("-views_count")
        .values("pk", "name", "max_views")
        # .order_by("-max_views")  # order in descending order
        # .values("pk", "name")  # fetch only pk and name
        # .distinct()[:4]  # remove duplicate and get only 4 records
    )
    category_ids = [
        top_category["pk"] for top_category in top_categories
    ]  #  [2, 6, 5, 6]
    order_by_max_views = Case(
        *[
            When(
                id=category["pk"],
                then=category["max_views"]
                # When(id=2, then=11), When(id=6. then=2)
            )
            for category in top_categories
        ]
    )

    whats_new_categories = Category.objects.filter(
        pk__in=[top_category["pk"] for top_category in top_categories]
    )

    return {
        "categories": categories,
        "tags": tags,
        "top_categories": top_categories,
        "whats_new_categories": whats_new_categories,
    }
