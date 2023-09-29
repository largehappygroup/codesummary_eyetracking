public class MyClass {
  public void close() {
    Tabpanel tempPanel = null;
    View tempView = null;
    List<?> list;
    Enumeration<Tabbox> tabs = primaryTabMap.keys();

    while (tabs.hasMoreElements()) {
      list = tabs.nextElement().getTabpanels().getChildren();
      Iterator<?> itr = list.iterator();

      while (itr.hasNext()) {
        tempPanel = (Tabpanel) itr.next();
        tempView = (View) tempPanel.getChildren().get(0);
        tempView.deregisterView();
      }
    }
  }
}