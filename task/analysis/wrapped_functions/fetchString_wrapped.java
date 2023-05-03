public class MyClass {
    protected String fetchString(int register, int len) {
        int ret = getData(register, byteBuff, 8);
        char[] charBuff = new char[len];

        for (int i = 0; i < len; i++)
            charBuff[i] = (byteBuff[i] == 0 ? ' ' : (char) byteBuff[i]);
        return new String(charBuff, 0, len);
    }
}