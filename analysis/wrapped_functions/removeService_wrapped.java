public class ServiceRemover {
    public void removeService(String type) {
        CService service = (CService) services.get(type);

        if (service != null) {
            service.unsetContext();
            services.remove(type);
            fireServiceChanged(new CServiceEvent(this, service, CServiceEvent.REMOVED));
        }
    }
}