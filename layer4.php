<!DOCTYPE html>
<html lang="en">
<head>
	<title>LAYER 4 API</title>
	<!--
	This is API created for Ts3 Bot to detect the DDoS attack on VPS  where is Ts3 server and Ts3 Bot.
	42O Productions    
	-->
</head>
</html>
<?php  
$x = time() * 1000;

function mean($first, $second, $time, $zone)
{
	$y = ($second - $first);
	if ($zone == 'US') {
		$y *= 8;
	}
	echo sprintf("%.2f", $y);
	//return json_encode(array($time, $y));
}

function dataFetch($type, $interface)
{
	$data1 = @file_get_contents("/sys/class/net/{$interface}/statistics/{$type}_bytes");
	sleep(1);
	$data2 = @file_get_contents("/sys/class/net/{$interface}/statistics/{$type}_bytes");
	return [$data1, $data2];
}

$rtx = dataFetch("rx", "eth0");
echo mean($rtx[0], $rtx[1], $x, 'US');
?>