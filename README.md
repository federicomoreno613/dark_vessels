# Dark Vessles

## Detección y Segmentación de Embarcaciones en Imágenes SAR utilizando Deep Learning

El fenómeno de la pesca ilegal, no declarada y no reglamentada (IUU) representa un problema mundial que afecta los sistemas ecológicos y ocasiona pérdidas significativas para la industria pesquera y los gobiernos a nivel global. Para combatir esta práctica y sus impactos devastadores, como la disminución de la biodiversidad marina y el fomento de la piratería, se llevan a cabo esfuerzos de monitoreo, control y vigilancia (MCS)\cite{Agnew2009}. Una de las principales dificultades en la vigilancia marítima es la presencia de embarcaciones "oscuras", que desactivan sus sistemas de Identificación Automática (AIS)\cite{FAO2016} para evadir la detección durante actividades ilícitas.

## Elección del Conjunto de Datos SARFish

Para el desarrollo de este proyecto, se seleccionó el conjunto de datos SARFish\cite{SARFishDataset} presentado originalmente presentado en el año 2022 con la finalidad de entrenamiento y validación de algoritmos de aprendizaje profundo en las tareas de detección, clasificación y regresión del largo de objetos marítimos.

Este dataset consiste en  753 pares de imágenes de Radar de Apertura Sintética (SAR) de la misión Sentinel-1 y se construye por encima del  xView3-SAR dataset\cite{xView3SAR} proveyendo productos Single Look Complex (SLC) como Ground Range Detected (GRD) junto con los objetos anotados en posiciones y cuadros delimitados (Bouding Boxes en formato MS COCO ). 

Cada anotación se complemente con con registros AIS/VM y contiene información jerárquica respecto a tipo de barco y medidas de largo de embarcación. Se encuentran identificados 143,000 objetos marítimos, cada uno con un un nivel de confianza. 

La resolución espacial cercana a los 10 metros por pixel, ofrece la granularidad necesaria para la identificación precisa de objetos marítimos desde una perspectiva satelital.La elección se fundamenta en la capacidad del SARFish de proporcionar una amplia gama de escenarios marítimos detallados, esenciales para el análisis y detección de embarcaciones involucradas en pesca IUU. 


### Elección de una pregunta
¿Cómo pueden los métodos de Deep Learning mejorar la precisión y eficiencia en la detección y segmentación de barcos para el dataset SARFish?


\bibitem{Agnew2009}
Agnew, D. J., Pearce, J., Pramod, G., Peatman, T., Watson, R., Beddington, J. R., \& Pitcher, T. J. (2009). \emph{Estimating the worldwide extent of illegal fishing.} PLoS ONE, 4(2), e4570. doi: 10.1371/journal.pone.0004570. Disponible en: \url{https://doi.org/10.1371/journal.pone.0004570}.

\bibitem{FAO2016}
Organización de las Naciones Unidas para la Alimentación y la Agricultura (FAO). (2016). \emph{El estado mundial de la pesca y la acuicultura 2016}. Disponible en: \url{http://www.fao.org/3/a-i5555s.pdf}.


\bibitem{SARFishDataset}
T. -T. Cao et al., \emph{"SARFish: Space-Based Maritime Surveillance Using Complex Synthetic Aperture Radar Imagery,"} 2022 International Conference on Digital Image Computing: Techniques and Applications (DICTA), Sydney, Australia, 2022, pp. 1-8, doi: 10.1109/DICTA56598.2022.10034640.
