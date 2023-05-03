public class TagTester {
    public void testSetExample() {
        System.out.println( "testSetExample" );
        String testString = "<tag:foo>|n";
        testString += "|t<tag:bar />";
        testString += "</tag:foo>";
        Tag tag = new Tag();
        tag.setExample( testString );
        assertEquals( tag.getExample(), testString );
    }
}