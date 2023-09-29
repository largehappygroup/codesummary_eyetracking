public class ChecklistItemCreator {
    
    private static final String KEY_LIST_ID = "list_id";
    private static final String KEY_IS_DONE = "is_done";
    private static final String KEY_ITEM = "item";
    private static final String CHECKLIST_ITEM_TBL = "checklist_item_tbl";
    
    private SQLiteDatabase mDb;
    
    public ChecklistItemCreator(SQLiteDatabase db) {
        mDb = db;
    }
    
    public long createChecklistItem(long listId, String item, boolean isDone) {
        ContentValues values = new ContentValues();
        values.put(KEY_LIST_ID, listId);
        values.put(KEY_IS_DONE, isDone);
        values.put(KEY_ITEM, item);
        return mDb.insert(CHECKLIST_ITEM_TBL, null, values);
    }
}