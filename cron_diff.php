<!DOCTYPE html>
<html>
<head>
<title>Pandora ProtoDUNE-SP Validation</title>
<h1>Pandora ProtoDUNE-SP Validation</h1>
<link rel="stylesheet" type="text/css" href="mystyle.css">
</head>

<?php
$date1 = $_POST['Date1'];
$date2 = $_POST['Date2'];

$myversion1 = $_POST['SoftwareVersion1'];
$myversion2 = $_POST['SoftwareVersion2'];

$yy = substr($date1,6,2);
$mm = substr($date1,3,2);
$dd = substr($date1,0,2);

$newDateFormat1 = "20".$yy."_".$mm."_".$dd;

$yy = substr($date2,6,2);
$mm = substr($date2,3,2);
$dd = substr($date2,0,2);

$newDateFormat2 = "20".$yy."_".$mm."_".$dd;

if (!empty($date1))
{
    echo "<h4>Date 1 : $newDateFormat1</h4>";
}
if (!empty($date2))
{
    echo "<h4>Date 2 : $newDateFormat2</h4>";
}

$mydir1 = "CronResults/".$newDateFormat1."/".$myversion1."/RootFiles";
$mydir2 = "CronResults/".$newDateFormat2."/".$myversion2."/RootFiles";

$tableOutput1 = $mydir1. '/TableOutput.txt';
$tableOutput2 = $mydir2. '/TableOutput.txt';

if (file_exists($tableOutput1) && file_exists($tableOutput2))
{
    $output = shell_exec("diff -u $tableOutput1 $tableOutput2 | ./diff2html.sh");
    echo $output;
    file_put_contents('tmp.php', $output);
    include("tmp.php");
}

?>

</html> 

