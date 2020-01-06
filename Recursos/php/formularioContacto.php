<?php

    $error = ""; $mensajeExito = "";

    if ($_POST) {
        
        if (!$_POST["email"]) {
            
            $error .= "Es obligatorio una dirección de email.<br>";
            
        }
        
        if (!$_POST["contenido"]) {
            
            $error .= "El contenido del mensaje es obligatorio.<br>";
            
        }
        
        if (!$_POST["asunto"]) {
            
            $error .= "El campo asunto del mensaje es obligatorio.<br>";
            
        }
        
        if ($_POST['email'] && filter_var($_POST["email"], FILTER_VALIDATE_EMAIL) === false) {
            
            $error .= "Correo electrónico no válido.<br>";
            
        }
        
        if ($error != "") {
            
            $error = '<div class="alert alert-danger" role="alert"><p>Hubo algún error en el formulario:</p>' . $error . '</div>';
            
        } else {
            
            $emailA = "me@mydomain.com";
            
            $asunto = $_POST['asunto'];
            
            $contenido = $_POST['contenido'];
            
            $cabeceras = "From: ".$_POST['email'];
            
            if (mail($emailA, $asunto, $contenido, $cabeceras)) {
                
                $mensajeExito = '<div class="alert alert-success" role="alert">Mensaje enviado con éxito, nos pondremos en contacto pronto!</div>';
                
                
            } else {
                
                $error = '<div class="alert alert-danger" role="alert"><p><strong>El mensaje no pudo ser enviado, por favor inténtalo más tarde</div>';
                
                
            }
            
        }
        
        
        
    }

?>

<!DOCTYPE html>
<html lang="es">
  <head>
    <!-- Required meta tags always come first -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta http-equiv="x-ua-compatible" content="ie=edge">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.2/css/bootstrap.min.css" integrity="sha384-y3tfxAZXuh4HwSYylfB+J125MxIs6mR5FOHamPBG064zB+AFeWH94NdvaCBm8qnd" crossorigin="anonymous">
  </head>
  <body>
      
      <div class="container">
      
    <h1>Contacta con nosotros</h1>
      
      <div id="error"><? echo $error.$mensajeExito; ?></div>
      
      <form method="post">
            <fieldset class="form-group">
                  <label for="email">Dirección de email</label>
                  <input type="email" class="form-control" id="email" name="email" placeholder="Introduce email">
                  <small class="text-muted">Nunca compartiremos tu email con nadie.</small>
            </fieldset>
            <fieldset class="form-group">
                  <label for="asunto">Asunto</label>
                  <input type="text" class="form-control" id="asunto" name="asunto" >
            </fieldset>
            <fieldset class="form-group">
                  <label for="contenido">¿Qué te gustaría preguntarnos?</label>
                  <textarea class="form-control" id="contenido" name="contenido" rows="3"></textarea>
            </fieldset>
                  <button type="submit" id="submit" class="btn btn-primary">Enviar</button>
      </form>
          
        </div>

    <!-- jQuery first, then Bootstrap JS. -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.4/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.2/js/bootstrap.min.js" integrity="sha384-vZ2WRJMwsjRMW/8U7i6PWi6AlO1L79snBrmgiDpgIWJ82z8eA5lenwvxbMV1PAh7" crossorigin="anonymous"></script>
          
          
    <script type="text/javascript">
          
          $("form").submit(function(e) {
              
              var error = "";
              
              if ($("#email").val() == "") {
                  
                  error += "Campo email obligatorio.<br>"
                  
              }
              
              if ($("#asunto").val() == "") {
                  
                  error += "Campo asunto obligatorio.<br>"
                  
              }
              
              if ($("#contenido").val() == "") {
                  
                  error += "Campo contenido obligatorio.<br>"
                  
              }
              
              if (error != "") {
                  
                 $("#error").html('<div class="alert alert-danger" role="alert"><p><strong>Hubo algún error en el formulario</strong></p>' + error + '</div>');
                  
                  return false;
                  
              } else {
                  
                  return true;
                  
              }
          })
          
    </script>
          
  </body>
</html>