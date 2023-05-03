```java
public class FeedQuery {
    public List<FeedItem> getRelFeedItems(FeedItem feedItem) {
        final int feedId = feedItem.getFeed().getFeedId();
        final String sql = "select * from T_FeedItem where FEED_ID =" + feedId;
        return getPagedListByNativeSQL(FeedItem.class, sql, " id desc", 1, 20);
    }
}
```