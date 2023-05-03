public class CookieParser {
    private javax.servlet.http.HttpServletRequest servletRequest;

    public CookieParser(javax.servlet.http.HttpServletRequest servletRequest) {
        this.servletRequest = servletRequest;
    }

    private String getUserNameFromCookie() throws Exception {
        String userName = null;
        // get user name
        Cookie[] cookies = servletRequest.getCookies();

        for (int i = 0; i < cookies.length; i++) {
            Cookie cookie = cookies[i];

            if (cookie != null && cookie.getName().equals("platform.username")) {
                String value = cookie.getValue();
                userName = DesEncrypter.getInstance().decrypt(value);
                break;
            }
        }
        return userName;
    }
}