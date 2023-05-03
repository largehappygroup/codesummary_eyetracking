public class DigitAdder {
    private String value;
    private boolean update;
    private boolean minus;
    private boolean comma;

    public void addDigit(char digit) {
        if (digit == '0' && value.equals("0")) return;
        if (value.equals("0")) value = "";
        if (update) {
            value = "";
            minus = false;
            comma = false;
        }
        update = false;
        value += digit;
        showValue();
    }

    private void showValue() {
        System.out.println(value);
    }
}