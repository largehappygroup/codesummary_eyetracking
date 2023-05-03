public class DateManager {
    private List<Date> dates;

    public DateManager() {
        dates = new ArrayList<>();
    }

    public boolean add(Date date) {
        if (dates.contains(date))
            return false;

        boolean added = false;
        for (int i = 0; i < dates.size() && !added; i++) {
            Date nextDate = dates.get(i);

            if (date.before(nextDate)) {
                dates.add(i, date);
                added = true;
            }
        }
        if (!added) {
            dates.add(date);
        }
        return true;
    }
}