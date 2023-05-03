public class TestClass {
    public void testInvoke() throws Exception {
        transport.setRemoteService("TravelProcess");
        call.setOperation("initiate");
        call.addParameter("x", XMLType.XSD_STRING, ParameterMode.IN);
        call.setReturnType(XMLType.XSD_STRING);

        String result = (String) call.invoke(new Object[]{"anything"});

        assertEquals(DUMMY_RESULT, result);
    }
}