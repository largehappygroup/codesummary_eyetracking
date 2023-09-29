public class ChartData {

    public XYDataset createDataset(double[] values, String name) {
        final XYSeries series = new XYSeries(name);

        for (int i = 0; i < values.length; i++) {
            series.add(i, values[i]);
        }
        final XYSeriesCollection collection = new XYSeriesCollection();
        collection.addSeries(series);

        return collection;
    }
}