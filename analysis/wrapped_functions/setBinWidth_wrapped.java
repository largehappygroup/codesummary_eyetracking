public class BinWidthSetter {
    public void setBinWidth(double new_bin_width) {
        double old_bin_width = binWidth;
        binWidth = new_bin_width;
        pcs.firePropertyChange("binWidth",
                new Double(old_bin_width),
                new Double(new_bin_width));
        repaint();
    } // setBinWidth(double)

    private double binWidth;
    private final PropertyChangeSupport pcs = new PropertyChangeSupport(this);

    public void addPropertyChangeListener(PropertyChangeListener listener) {
        pcs.addPropertyChangeListener(listener);
    }

    public void removePropertyChangeListener(PropertyChangeListener listener) {
        pcs.removePropertyChangeListener(listener);
    }

    private void repaint() {
        // implementation of repaint method
    }
}