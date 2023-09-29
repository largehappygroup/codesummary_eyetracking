public class GlobalElementParser {
    private GlobalDefMap globalDefMap;

    public GlobalElementParser(GlobalDefMap globalDefMap) {
        this.globalDefMap = globalDefMap;
    }

    public void getGlobalElements(Document doc, File file) {
        if (doc == null) {
            return;
        }
        List list = doc.selectNodes("/xsd:schema/xsd:element");

        for (Iterator iter = list.iterator(); iter.hasNext();) {
            Element element = (Element) iter.next();
            String name = element.attributeValue("name");
            GlobalElement g = new GlobalElement(element, file);
            // System.out.println ( g.toString() );
            try {
                globalDefMap.setValue(name, g);
            } catch (Exception e) {
                System.out.println(e.getMessage());
            }
        }
    }
}