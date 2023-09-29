public class JSPTest {
    public void testCookieGreaterThan() throws ServletException, JspException {
        GreaterThanTag gt = new GreaterThanTag();
        gt.setPageContext(pageContext);
        gt.setCookie(COOKIE_KEY);
        gt.setValue(LESSER_VAL);

        assertTrue("Cookie Value (" + GREATER_VAL + ") is greater than value (" + LESSER_VAL + ")", gt.condition());
    }
}