public class QueryCounter {
    private PersistenceBroker pride2Broker;

    protected int countQuery(final Query query) throws PersistenceException {
        if (query != null) {
            if (pride2Broker != null) {
                return pride2Broker.getCount(query);
            } else {
                throw new PersistenceException("Query called on uninitialized PersistenceBroker", null);
            }
        } else {
            throw new PersistenceException("No query specified!", null);
        }
    }
}