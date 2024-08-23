-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 23-08-2024 a las 01:57:07
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `db_inventario_ur`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cuentadante`
--

CREATE TABLE `cuentadante` (
  `id` int(11) NOT NULL,
  `documento` varchar(12) NOT NULL,
  `nombres` varchar(40) NOT NULL,
  `apellidos` varchar(40) NOT NULL,
  `correo` varchar(50) NOT NULL,
  `celular` varchar(12) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `cuentadante`
--

INSERT INTO `cuentadante` (`id`, `documento`, `nombres`, `apellidos`, `correo`, `celular`) VALUES
(6, '9975658', 'Jose Fernando', 'Murillo Arango', 'jfmurillo@sena.edu.co', '3113644482');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `equipo`
--

CREATE TABLE `equipo` (
  `id` int(11) NOT NULL,
  `serial` varchar(20) NOT NULL,
  `marca` varchar(20) NOT NULL,
  `modelo` varchar(15) NOT NULL,
  `tipo` varchar(10) NOT NULL,
  `fecha_compra` date NOT NULL,
  `garantia` int(11) NOT NULL,
  `clasificacion` varchar(12) NOT NULL,
  `cuentadante_id` int(11) NOT NULL,
  `ubicacion_id` int(11) NOT NULL,
  `proveedor_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `equipo`
--

INSERT INTO `equipo` (`id`, `serial`, `marca`, `modelo`, `tipo`, `fecha_compra`, `garantia`, `clasificacion`, `cuentadante_id`, `ubicacion_id`, `proveedor_id`) VALUES
(5, '123-BC', 'Dell', 'model 1', 'Todo en un', '2024-08-01', 12, 'Administrati', 6, 1, 2),
(6, '123456987', 'Dell', 'One touch', 'Laptop', '2024-08-15', 12, 'Administraci', 6, 1, 4),
(7, '1111111', 'hp', 'hp 2', 'All in one', '2020-12-24', 5, 'Formación', 6, 1, 5),
(8, '147852', 'Lenovo', 'Len159', 'Laptop', '2023-10-25', 15, 'Formación', 6, 1, 5);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `proveedor`
--

CREATE TABLE `proveedor` (
  `id` int(11) NOT NULL,
  `nit` varchar(15) NOT NULL,
  `razon_social` varchar(80) NOT NULL,
  `direccion` varchar(50) NOT NULL,
  `telefono` varchar(12) NOT NULL,
  `email` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `proveedor`
--

INSERT INTO `proveedor` (`id`, `nit`, `razon_social`, `direccion`, `telefono`, `email`) VALUES
(2, '89236985', 'Proveedor 1', 'Manizales', '89656', 'pro@gmail.com'),
(4, '7896635466', 'Apples', 'Pereira', '58986', 'perira@yahoo.com'),
(5, '7412253036', 'Mercaldas', 'Cra 24', '7896652', 'mercaldas@yahoo.es');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ubicacion`
--

CREATE TABLE `ubicacion` (
  `id` int(11) NOT NULL,
  `nombre` varchar(25) NOT NULL,
  `descripcion` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `ubicacion`
--

INSERT INTO `ubicacion` (`id`, `nombre`, `descripcion`) VALUES
(1, 'aula 202', 'Segundo piso');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `cuentadante`
--
ALTER TABLE `cuentadante`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `documento` (`documento`);

--
-- Indices de la tabla `equipo`
--
ALTER TABLE `equipo`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `serial` (`serial`),
  ADD KEY `equ_cue` (`cuentadante_id`),
  ADD KEY `equ_ubi` (`ubicacion_id`),
  ADD KEY `equ_pro` (`proveedor_id`);

--
-- Indices de la tabla `proveedor`
--
ALTER TABLE `proveedor`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nit` (`nit`),
  ADD UNIQUE KEY `razon_social` (`razon_social`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indices de la tabla `ubicacion`
--
ALTER TABLE `ubicacion`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nombre` (`nombre`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `cuentadante`
--
ALTER TABLE `cuentadante`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `equipo`
--
ALTER TABLE `equipo`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de la tabla `proveedor`
--
ALTER TABLE `proveedor`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `ubicacion`
--
ALTER TABLE `ubicacion`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `equipo`
--
ALTER TABLE `equipo`
  ADD CONSTRAINT `equ_cue` FOREIGN KEY (`cuentadante_id`) REFERENCES `cuentadante` (`id`),
  ADD CONSTRAINT `equ_pro` FOREIGN KEY (`proveedor_id`) REFERENCES `proveedor` (`id`),
  ADD CONSTRAINT `equ_ubi` FOREIGN KEY (`ubicacion_id`) REFERENCES `ubicacion` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
