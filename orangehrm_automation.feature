Feature: Automatización de la contratación de una persona en OrangeHRM

  @orangehrm
  Escenario: Iniciar sesión y contratar una persona
    Dado que estoy en la página de inicio de sesión de OrangeHRM
    Cuando ingreso credenciales válidas
    Entonces debería estar iniciada la sesión
    Cuando navego a la página de Reclutamiento
    Y hago clic en el botón "Agregar"
    Y lleno el formulario de reclutamiento
    Entonces la persona debería ser contratada