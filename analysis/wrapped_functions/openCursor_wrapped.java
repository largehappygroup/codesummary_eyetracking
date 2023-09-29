public class CursorOpener {
    public Cursor openCursor(Context context, String selection, String[] selectionArgs) {
        if (mSourcesUri == null) {
            throw new NullPointerException("Sources uri not set.");
        }
        return context.getContentResolver().query(mSourcesUri, mProjection, selection, selectionArgs, Sources.SourcesTable.NAME);
    }
}