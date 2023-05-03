public class Table {
    private Map<String, Column> colMap;
    private List<Column> pkColumns;
    private String name;

    public void addPKColumn(String aPKColName) throws IllegalArgumentException {
        Column col = (Column) colMap.get(aPKColName);

        if (col == null) {
            throw new IllegalArgumentException("The column |" + aPKColName + "| does not belong to the table |"
                    + name + "|");
        }

        pkColumns.add(col);
    }
}