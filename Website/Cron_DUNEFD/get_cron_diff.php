<!DOCTYPE html>
<html>
<head>
<title>Pandora DUNEFD Validation</title>
<h1>Pandora DUNEFD Validation</h1>
<link rel="stylesheet" type="text/css" href="mystyle.css">

<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>jQuery UI Datepicker - Default functionality</title>
<link rel="stylesheet" href="//code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css">
<link rel="stylesheet" href="/resources/demos/style.css">
<script src="https://code.jquery.com/jquery-1.12.4.js"></script>
<script src="https://code.jquery.com/ui/1.12.1/jquery-ui.js"></script>
<script>
$( function() 
{
    $( ".datepicker" ).datepicker({
        dateFormat: "dd-mm-y",
        minDate: new Date(2018, 6 - 1, 20),
        maxDate: "+0D"
    });
} );
</script>
</head>

<body>
<form action="cron_diff.php" name="Filter" method="POST">
    Diff Date One:
    <input type="text" class="datepicker" name="Date1"/>

    <select name="SoftwareVersion1">
    Version:
        <option value="mcc10_larsoft_v06_60_00_nue_SpaceChargeEffectOff" <?php echo ($_POST['myversion'] == 'mcc10_larsoft_v06_60_00_nue_SpaceChargeEffectOff') ? 'selected' : ''; ?> >mcc10_larsoft_v06_60_00_nue_SpaceChargeEffectOff</option>
        <option value="mcc10_larsoft_v06_60_00_numu_SpaceChargeEffectOff" <?php echo ($_POST['myversion'] == 'mcc10_larsoft_v06_60_00_numu_SpaceChargeEffectOff') ? 'selected' : ''; ?> >mcc10_larsoft_v06_60_00_numu_SpaceChargeEffectOff</option>
        <option value="mcc10_larsoft_v06_60_00_anu_SpaceChargeEffectOff" <?php echo ($_POST['myversion'] == 'mcc10_larsoft_v06_60_00_anu_SpaceChargeEffectOff') ? 'selected' : ''; ?> >mcc10_larsoft_v06_60_00_anu_SpaceChargeEffectOff</option>
    </select>
    <br/>

    Diff Date Two:
    <input type="text" class="datepicker" name="Date2"/>

    <select name="SoftwareVersion2">
    Version
        <option value="mcc10_larsoft_v06_60_00_nue_SpaceChargeEffectOff" <?php echo ($_POST['myversion'] == 'mcc10_larsoft_v06_60_00_nue_SpaceChargeEffectOff') ? 'selected' : ''; ?> >mcc10_larsoft_v06_60_00_nue_SpaceChargeEffectOff</option>
        <option value="mcc10_larsoft_v06_60_00_numu_SpaceChargeEffectOff" <?php echo ($_POST['myversion'] == 'mcc10_larsoft_v06_60_00_numu_SpaceChargeEffectOff') ? 'selected' : ''; ?> >mcc10_larsoft_v06_60_00_numu_SpaceChargeEffectOff</option>
        <option value="mcc10_larsoft_v06_60_00_anu_SpaceChargeEffectOff" <?php echo ($_POST['myversion'] == 'mcc10_larsoft_v06_60_00_anu_SpaceChargeEffectOff') ? 'selected' : ''; ?> >mcc10_larsoft_v06_60_00_anu_SpaceChargeEffectOff</option>
    </select>
    <br/>

    <input type="submit" name="submit" value="Enter"/>
</form>

</body>
</html>

