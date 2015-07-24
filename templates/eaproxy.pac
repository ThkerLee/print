/*
 *	Super Proxy Script
 *	by Eternalasia MIS 2006-11-01
*/



function FindProxyForURL(url, host)
{
	/*------------2011-04-15-----alert(host)--------------------*/
	if (isInNet(host, "210.75.23.178","255.255.255.255")||
	    isInNet(host, "203.166.220.98","255.255.255.255")||
	    isInNet(host, "121.52.226.199","255.255.255.255")||
	    isInNet(host, "183.129.207.248","255.255.255.255")||
	    isInNet(host, "202.170.136.10","255.255.255.255")
	){
	   return "PROXY cache1.eascs.com:3128; DIRECT";
	}
	/*-------------2011-04-15------------------------*/

        if (isInNet(host,"172.0.0.0","255.0.0.0") || dnsDomainIs(host, ".eascs.com") || dnsDomainIs(host, ".esunnyloan.com") || dnsDomainIs(host, ".hqew.com") || dnsDomainIs(host, ".51job.com") || dnsDomainIs(host, ".zhaopin.com")|| dnsDomainIs(host, ".ccb.com") || dnsDomainIs(host,".eclink.net.cn") || dnsDomainIs(host, ".ksf.com.cn") || dnsDomainIs(host, ".icbc.com.cn") || dnsDomainIs(host, ".chinaport.gov.cn") || dnsDomainIs(host, ".midea.com.cn") || dnsDomainIs(host, ".cmbchina.com") || dnsDomainIs(host, ".cjol.com") || isPlainHostName(host)){return "DIRECT";
       } 
	else 
	{	var myip = myIpAddress();
		/* -----------MSN专用服务器 2008-01-30--------------*/
		if(dnsDomainIs(host, ".msn.com") || dnsDomainIs(host, ".live.com") || dnsDomainIs(host, ".hotmail.com") || dnsDomainIs(host, ".live.cn") || dnsDomainIs(host, ".microsoft.com") ){
		return "PROXY cache0.eascs.com:3128; PROXY cache1.eascs.com:3128; PROXY cache5.eascs.com:3128";}
		/*-----------------HK Site Direct---------------------*/
		if (isInNet(myip, "172.29.14.0", "255.255.255.0")){return "DIRECT";}
		if (isInNet(myip, "172.29.15.0", "255.255.255.0")){return "DIRECT";}
		/*--if (isInNet(myip, "172.16.0.0", "255.255.0.0")){return "DIRECT";} --*/
		/*----------------------------------------------------*/
		if (isInNet(myip, "172.29.101.0", "255.255.255.0")){
			return "PROXY cache0.eascs.com:3128; PROXY cache1.eascs.com:3128; DIRECT";}
		if (isInNet(myip, "172.29.10.0", "255.255.255.0") || isInNet(myip, "172.29.11.0", "255.255.255.0")){
			return "PROXY cache2.eascs.com:3128; PROXY cache1.eascs.com:3128; PROXY cache0.eascs.com:3128; DIRECT";}
		if (isInNet(myip, "172.29.16.0", "255.255.255.0")){
			return "PROXY cache3.eascs.com:3128; PROXY cache1.eascs.com:3128; PROXY cache0.eascs.com:3128; DIRECT";
		} else {
			if (isInNet(myip, "0.0.0.0", "0.0.0.0")){

				var n = URLhash2(url) % 5;
	if (n < 2)
		return "PROXY cache1.eascs.com:3128; PROXY cache1.eascs.com:3128; PROXY cache4.eascs.com:3128; PROXY cache5.eascs.com:3128; DIRECT";
	if (n < 3)
		return "PROXY cache1.eascs.com:3128; PROXY cache4.eascs.com:3128; PROXY cache5.eascs.com:3128; PROXY cache0.eascs.com:3128; DIRECT";
	if (n < 4)
		return "PROXY cache4.eascs.com:3128; PROXY cache5.eascs.com:3128; PROXY cache0.eascs.com:3128; PROXY cache1.eascs.com:3128; DIRECT";
	if (n < 5)
		return "PROXY cache4.eascs.com:3128; PROXY cache0.eascs.com:3128; PROXY cache1.eascs.com:3128; PROXY cache4.eascs.com:3128; DIRECT";

				} else { return "DIRECT";}}}}

function URLhash2(name)
{
var  cnt=0; 
var  dirptr=0;

	var str=name.toLowerCase(name);
	if ( str.length ==0) {
	 	return cnt;	
	}
	for(var i=str.length - 1;i >=0 ; i--) {
		if ( str.substring(i,i +1) == '/' ) {
			dirptr = i+1 ;
			break;
		}
	}

	for(var i=0;i < dirptr; i++) {
	   var ch= atoi(str.substring(i,i + 1));
		cnt = cnt + ch;
	}

	return cnt ;
}

function atoi(charstring)
{

	if ( charstring == "a" ) return 0x61; if ( charstring == "b" ) return 0x62;
	if ( charstring == "c" ) return 0x63; if ( charstring == "d" ) return 0x64;
	if ( charstring == "e" ) return 0x65; if ( charstring == "f" ) return 0x66;
        if ( charstring == "g" ) return 0x67; if ( charstring == "h" ) return 0x68;
	if ( charstring == "i" ) return 0x69; if ( charstring == "j" ) return 0x6a;
	if ( charstring == "k" ) return 0x6b; if ( charstring == "l" ) return 0x6c;
	if ( charstring == "m" ) return 0x6d; if ( charstring == "n" ) return 0x6e;
	if ( charstring == "o" ) return 0x6f; if ( charstring == "p" ) return 0x70;
	if ( charstring == "q" ) return 0x71; if ( charstring == "r" ) return 0x72;
	if ( charstring == "s" ) return 0x73; if ( charstring == "t" ) return 0x74;
	if ( charstring == "u" ) return 0x75; if ( charstring == "v" ) return 0x76;
	if ( charstring == "w" ) return 0x77; if ( charstring == "x" ) return 0x78;
	if ( charstring == "y" ) return 0x79; if ( charstring == "z" ) return 0x7a;
	if ( charstring == "0" ) return 0x30; if ( charstring == "1" ) return 0x31;
	if ( charstring == "2" ) return 0x32; if ( charstring == "3" ) return 0x33;
	if ( charstring == "4" ) return 0x34; if ( charstring == "5" ) return 0x35;
	if ( charstring == "6" ) return 0x36; if ( charstring == "7" ) return 0x37;
	if ( charstring == "8" ) return 0x38; if ( charstring == "9" ) return 0x39;
	if ( charstring == "." ) return 0x2e;
	return 0x20;
}

