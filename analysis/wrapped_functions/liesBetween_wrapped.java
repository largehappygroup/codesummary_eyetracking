public class MyClass {
    private static final double ACCURACY = 0.0001;

    private boolean liesBetween(double x1, double x2, double x3) {
        if ((x1 <= x2) && (x3 >= x1 - ACCURACY && x3 <= x2 + ACCURACY))
            return true;
        if ((x1 >= x2) && (x3 >= x2 - ACCURACY && x3 <= x1 + ACCURACY))
            return true;

        return false;
    }
}