from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait # no deja que el script ejecute la página hasta que halla cargado
from selenium.webdriver.support import expected_conditions as EC # ayuda a buscar información si existe o no 
from selenium.webdriver.common.by import By # escoger elementos, hacer consultas 



# agregar opciones de navegación 
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized') # iniciar con pantalla completa
options.add_argument('--disable-extensions') # desactivar extensiones



driver = webdriver.Chrome(options=options) # opciones para el navegador inicie (pantalla maxima - extensiones desactivadas)
driver.get('https://www.tupi.com.py/') # abrir el navegador 

# hacemos que espere hasta que la página cargue todo, y agregamos 5 segundos. 
# hasta (until) el EC que es para saber la existencia .element_to_be_clickable() busque elemento clickeable
# BY para hacer alguna consulta EN ese caso algun CSS y copiar la clase del css de busqueda 
# send_keys es para escribir y enviar al palabra a buscar 
WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input#search.form-control.search-field'))).send_keys('teclados')
WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'i.ec.ec-search'))).click()

# Esperar a que la página cargue completamente
# Visibility of element located -> espera que los elementos sean visibles
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.product_unit.product')))

# Encontrar todos los elementos de productos en forma de contenedores
productos = driver.find_elements(By.CSS_SELECTOR, '.product_unit.product')
# Iterar sobre los productos para encontrar los que tienen la imagen esperada
i=0
for producto in productos:
    try:
        # verificar en el contendor si se encuentra la imagen de lo contrario lanza una excepción
        imagen_element = producto.find_element(By.CSS_SELECTOR, '.media_header_bubbles img') 
        # una vez encontrado se procede a guardar en la variable los elementos de la etiqueta <img>
        imagen_src = imagen_element.get_attribute('src')
        if 'BURBUJA_VAC.png' in imagen_src: # se comprueba que la imagen sea la indicada en este caso es la imagen de vuelta en clases
            # verifica si existe la etiqueta a donde esta el nombre del producto
            nombre_producto_element = producto.find_element(By.CSS_SELECTOR, '.nombre_producto_ug a') 
            nombre_producto = nombre_producto_element.text.strip() # extrae el texto del elemento
            precio_producto = producto.find_element(By.CSS_SELECTOR, '.price-add-to-cart a')
            precio_producto_imp = precio_producto.text.strip()
            url = producto.find_element(By.CSS_SELECTOR, '.media-body a')
            getUrl = url.get_attribute('href')
            i=i+1
            print(f"Nombre del producto[{i}]: {nombre_producto.replace('ver detalles','')}")
            print(f"Precio: {precio_producto_imp}")
            print(f"Link: {getUrl}")
            print("-"*51,"\n")
            
    except:
       pass

terminar= input("Presionar ENTER para terminar........\n")
driver.quit()