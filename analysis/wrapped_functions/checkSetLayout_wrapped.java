public class LayoutChecker {
    private Filter filter;
    private JTable fieldList;

    public LayoutChecker(Filter filter, JTable fieldList) {
        this.filter = filter;
        this.fieldList = fieldList;
    }

    private void checkSetLayout(int layout, String field) {
        filter.setLayoutIndex(layout);
        assertEquals("The layout Index was " + filter.getLayoutIndex()
                + " and not " + layout, layout, filter.getLayoutIndex());

        String fld = fieldList.getValueAt(1, 0).toString();
        assertEquals("Expected field '" + field + "' but got " + fld, field, fld);
    }
}