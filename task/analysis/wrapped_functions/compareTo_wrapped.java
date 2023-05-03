public class TPoint implements Comparable<TPoint> {
    private int value;
    private int tstamp;

    public TPoint(int value, int tstamp) {
        this.value = value;
        this.tstamp = tstamp;
    }

    public int compareTo(TPoint o) {
        if ((this.value == o.value()) && (this.tstamp == o.tstamp())) {
            return 0;
        } else if (this.tstamp > o.tstamp) {
            return 1;
        } else if (this.tstamp < o.tstamp) {
            return -1;
        } else if (this.value > o.value) {
            return 1;
        }
        return -1;
    }

    public int value() {
        return value;
    }

    public int tstamp() {
        return tstamp;
    }
}