public class Processor {
    public void process( WorkerIsReadyMessageHandle handle, ServiceManager serviceManager ) {
        WorkerIsReadyProcessorRequestTO to = new WorkerIsReadyProcessorRequestTO();
        ServiceID workerID = serviceManager.getSenderServiceID();

        to.setWorkerAddress( workerID.toString() );
        to.setWorkerContainerID( workerID.getContainerID().toString() );
        OurGridRequestControl.getInstance().execute( to, serviceManager );
    }
}