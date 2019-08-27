def main():
	countdown(5)

def countdown(i):
	print(i)
	if i==0:
		return
	else:
		countdown(i-1)

main()

#https://www.hackerearth.com/practice/algorithms/graphs/depth-first-search/tutorial/
#https://dev.to/s_awdesh/double-pivot-quick-sort--javas-default-sorting-algorithm-1m4
#https://dev.to/s_awdesh/timsort-fastest-sorting-algorithm-for-real-world-problems--2jhd
#https://accenture.englishtown.com/campus/mypage/home
#Chicken34bonD
#Toronto01acN
#Summer2019Sky
#Acc2348-0
#154132Bet..
#350 - onSelectAutofill 
#503 - selectTransaction
#00736638 
#http://certprod-acn.cs8.force.com/certprep/SA_SiteAuthLD

z-index: 100;
display: block;
position: absolute;


#2137207

#SFSC-180
#SFSC-181
#SFSC-187  34 -> 59
#https://mylearning.accenture.com/myl-ui/learner/course/id/1222229   
#32

"""
@TestVisible
    public static void mergeSharedAcccounts(List<Vendor__c> vendors) {
        Map<String, Vendor__c> sdmVendors = new Map<String, Vendor__c>();
        Map<String, Vendor__c> lclVendors = new Map<String, Vendor__c>();
        List<Vendor__c> sharedVendors = new List<Vendor__c>();
        
        String normalized =  '';
        Boolean isLCL = true;
        
        //Over all vendors obtained when trigger is flagged, get the SDM and LCL vendors that are active. 
        for(Vendor__c vendor : vendors){
            normalized = (((vendor.Name).toUpperCase()).normalizeSpace());
            //.substring(0, 5)
            
            if(vendor.Vendor_Status__c == 'Active') {
                if(vendor.Organization__c == 'SDM') {
                    sdmVendors.put(normalized, vendor);
                } else if(vendor.Organization__c == 'LCL') {
                    lclVendors.put(normalized, vendor);
                } else {
                    System.debug('No merge needed');
                }
            } else {
                System.debug('Status is not active');
            }
            
        }
        
        if(!sdmVendors.isEmpty()) {
            //Look for the LCL vendors who has the same name as an existing SDM vendor.
            sharedVendors = [SELECT Id, Name, Type__c FROM Vendor__c WHERE 
                                             Organization__c = 'LCL' AND Name IN: sdmVendors.keySet()];
        }
        
        if(!lclVendors.isEmpty()) {
            //Look for the SDM vendors who has the same name as an existing LCL vendor.
            sharedVendors = [SELECT Id, Name, Type__c, Merge_Vendor__c, (SELECT Vendor__c FROM VendorFactories__r) FROM Vendor__c WHERE 
                                             Organization__c = 'SDM' AND Name IN: lclVendors.keySet()];
            isLCL = false;
        }
        
        List<Vendor__c> vendorsToUpdate = new List<Vendor__c>();
        
        //If shared vendors were found and they have the same type:
        //1. Change their LCL organizations to ENT
        //2. Update the SDM merge vendor lookup
        //3. Update all vendor-factories to the merge vendor
        if(!sharedVendors.isEmpty()) {
            for(Vendor__c sharedVendor : sharedVendors) {
                normalized = ((sharedVendor.Name).toUpperCase()).normalizeSpace();
                
                if(isLCL) { 
                    if(sdmVendors.containsKey(normalized)) {
                        if((sharedVendor.Type__c).equals(sdmVendors.get(normalized).Type__c)) {
                            if(sdmVendors.get(normalized).Merge_Vendor__c == null) {
                                vendorsToUpdate.add(new Vendor__c(Id=sdmVendors.get(normalized).Id, Merge_Vendor__c=sharedVendor.Id));
                            }
                               
                            sharedVendor.Organization__c = 'ENT';
                            
                            //Pass all vendor-factories to the LCL vendor (This change can't be done now because reparenting is not allowed)
                            for(VendorFactory__c vendorFactories : sdmVendors.get(normalized).VendorFactories__r) {
                                //vendorFactories.Vendor__c = sharedVendor.Id;
                            }
                        }
                    }
                } else {
                    if(lclVendors.containsKey(normalized)) {
                        if((sharedVendor.Type__c).equals(lclVendors.get(normalized).Type__c)) {
                            if(sharedVendor.Merge_Vendor__c == null) {
                                sharedVendor.Merge_Vendor__c = lclVendors.get(normalized).Id;
                            } 
                            
                            vendorsToUpdate.add(new Vendor__c(Id=lclVendors.get(normalized).Id, Organization__c = 'ENT'));
                            
                            //Pass all vendor-factories to the LCL vendor (This change can't be done now because reparenting is not allowed)
                            for(VendorFactory__c vendorFactories : sharedVendor.VendorFactories__r) {
                                //vendorFactories.Vendor__c = lclVendors.get(normalized).Id;
                            }
                        }
                    }
                }
            } 
        }
        
        try {
            if(!vendorsToUpdate.isEmpty()) {
                update vendorsToUpdate;
                System.debug('vendors Updated');
            }
            if(!sharedVendors.isEmpty()) {
                update sharedVendors;
                System.debug('shared Updated');
            }
        } catch(exception e) {
            System.debug('Exception: '+e.getMessage());
        }

    }


"""



"""
@TestVisible
    public static void mergeSharedAcccounts(List<Vendor__c> vendors) {
        Map<Id, Vendor__c> sdmVendors = new Map<Id, Vendor__c>();
        Map<Id, Vendor__c> lclVendors = new Map<Id, Vendor__c>();
        String normalized =  '';
        
        //Over all vendors obtained when trigger is flagged, get the SDM vendors that are active. 
        for(Vendor__c vendor : vendors){
            if(vendor.Organization__c == 'SDM' && vendor.Vendor_Status__c == 'Active') {
                normalized = ((vendor.Name).toUpperCase()).normalizeSpace();
                sdmVendors.put(normalized, vendor);
            } else if(vendor.Organization__c == 'LCL' && vendor.Vendor_Status__c == 'Active') {
                normalized = ((vendor.Name).toUpperCase()).normalizeSpace();
                lclVendors.put(normalized, vendor);
            } else {
                System.debug('No merge needed');
            }
        }
        
        List<Vendor__c> sdmVendorsToUpdate = new List<Vendor__c>();
        
        //If LCL vendors were found and they have the same type as their shared vendor: 
        //1. Change their organizations to ENT
        //2. Get the SDM's IDs for a next update
        if(!sharedVendors.isEmpty() && !sdmVendors.isEmpty()) {
            for(Vendor__c sharedVendor : sharedVendors) {
                normalized = ((sharedVendor.Name).toUpperCase()).normalizeSpace();
                if((sharedVendor.Type__c).equals(sdmVendors.get(normalized).Type__c)) {
                 	sharedVendor.Organization__c = 'ENT';
                    sdmVendorsToUpdate.add(new Vendor__c(Id=sdmVendors.get(normalized).Id, Merge_Vendor__c=sharedVendor.Id));
                } 
            } 
        }
        
        //Update Merge Vendor lookup for SDM
        update sdmVendorsToUpdate;
    }



"""


#https://lclcallcenters--perf.cs9.my.salesforce.com/home/home.jsp?sdtd=1

#Status 302 means that the resource is temporarily located somewhere else, and the client/browser should continue requesting the original url.


#https://caricaturashd.com/hora-de-aventura-capitulos-completos-latino-online/

#I was thinking that a good approach can be add a lockup to the vendor object (same object) and called SharedVendor, 
#and add the parent (LCL) record, so everything stay on salesforce and you can search by, just need to review the audit (trigger) 
#and approvals process to see the impacts and the best way to isolate this records.

#SL Number
#plan



"""
int res = 0;
        int factor = a[a.length-1];
        int A_first = a[0];
        int limit = b[0];
        int[] A_factors = new int[10];
        int[] B_factors = new int[10];
        boolean isFactor = true;
        
        int i = 0;
        int j = 0;
        while(factor <= limit) {
            while(i <= a.length-1) {
                System.out.println("a[i]: "+a[i]);
                if((factor%a[i]) != 0) {
                    isFactor = false;
                }
                i++;
            }
            
            if(isFactor) {
                System.out.println("Factors: "+factor);
                if(A_factors[j] == 0) {
                    A_factors[j] = factor;
                    j++;
                }
            }
            factor+=a[a.length-1];
            System.out.println("New possible factor: "+factor);
        }
        
        return res;







i = 0;
        while(i < A_factors.length-1) {
            System.out.println("All A Factors: "+A_factors[i]);
      
      i++;
        }


"""