public class JoinTableRender {

  private Datamodel datamodel;

  public JoinTableRender(Datamodel datamodel) {
    this.datamodel = datamodel;
  }

  public String joinTableRender(Table from, Association association) {
    int n = 0;

    for (Association a : from.associations) {
      if (a.destination == association.destination) {
        ++n;
      }
    }
    return datamodel.getDisplayName(association.destination) + (n > 1 ? " on " + association.getName() : "");
  }
}