public class CascadingDeletion {
    public void deleteCascade( VyhladavaciAlgoritmus algorithm ) {
        //searcheds
        getHibernateTemplate().bulkUpdate(
            "DELETE Searched WHERE algorithm = ?",
                                      new Object[] { algorithm });
        //plans
        getHibernateTemplate().bulkUpdate(
            "DELETE SearchPlan WHERE algorithm = ?",
                 new Object[] { algorithm });
        //prefs
        getHibernateTemplate().bulkUpdate(
            "DELETE SearchPrefs WHERE algorithm = ?",
                      new Object[] { algorithm });
        //categories
        getHibernateTemplate().bulkUpdate(
            "DELETE SearchCategory WHERE algorithm = ?",
                                new Object[] { algorithm });
        delete( algorithm );
    }
}