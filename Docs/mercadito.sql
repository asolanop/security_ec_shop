-- phpMyAdmin SQL Dump
-- version 4.4.14
-- http://www.phpmyadmin.net
--
-- Servidor: localhost
-- Tiempo de generación: 09-11-2017 a las 03:52:52
-- Versión del servidor: 5.6.26
-- Versión de PHP: 5.6.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `mercadito`
--

--
-- Estructura de tabla para la tabla `Cart`
--

CREATE TABLE IF NOT EXISTS `Cart` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `Cart_Items`
--

CREATE TABLE IF NOT EXISTS `Cart_Items` (
  `cart_id` int(11) NOT NULL,
  `item_id` int(11) NOT NULL,
  `amount` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `Feedback`
--

CREATE TABLE IF NOT EXISTS `Feedback` (
  `id` int(11) NOT NULL,
  `comment` varchar(100) NOT NULL,
  `email` varchar(50) NOT NULL,
  `firstname` varchar(50) NOT NULL,
  `lastname` varchar(50) NOT NULL,
  `isAuth` tinyint(1) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `Items`
--

CREATE TABLE IF NOT EXISTS `Items` (
  `id` int(11) NOT NULL,
  `name` varchar(75) NOT NULL,
  `price` decimal(13,2) NOT NULL,
  `description` varchar(250) NOT NULL,
  `owner` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `log`
--

CREATE TABLE IF NOT EXISTS `log` (
  `id` int(11) NOT NULL,
  `query` varchar(500) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `Sessions`
--

CREATE TABLE IF NOT EXISTS `Sessions` (
  `id` varchar(32) NOT NULL DEFAULT '0',
  `created` datetime NOT NULL,
  `expiration` datetime NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `Users`
--

CREATE TABLE IF NOT EXISTS `Users` (
  `id` int(11) NOT NULL,
  `first_name` varchar(50) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(255) NOT NULL,
  `username` varchar(25) NOT NULL,
  `telephone` int(11) NOT NULL,
  `address` varchar(100) NOT NULL,
  `role` int(1) NOT NULL DEFAULT '0',
  `try_count` int(1) NOT NULL DEFAULT '0',
  `enable` tinyint(1) DEFAULT '1'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `Cart`
--
ALTER TABLE `Cart`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indices de la tabla `Cart_Items`
--
ALTER TABLE `Cart_Items`
  ADD PRIMARY KEY (`cart_id`,`item_id`),
  ADD KEY `cart_id` (`cart_id`),
  ADD KEY `item_id` (`item_id`);

--
-- Indices de la tabla `Feedback`
--
ALTER TABLE `Feedback`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `Items`
--
ALTER TABLE `Items`
  ADD PRIMARY KEY (`id`),
  ADD KEY `owner` (`owner`);

--
-- Indices de la tabla `log`
--
ALTER TABLE `log`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `Sessions`
--
ALTER TABLE `Sessions`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indices de la tabla `Users`
--
ALTER TABLE `Users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`),
  ADD UNIQUE KEY `username` (`username`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `Cart`
--
ALTER TABLE `Cart`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT de la tabla `Feedback`
--
ALTER TABLE `Feedback`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT de la tabla `Items`
--
ALTER TABLE `Items`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT de la tabla `log`
--
ALTER TABLE `log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT de la tabla `Users`
--
ALTER TABLE `Users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
  
DELIMITER $$
--
-- Procedimientos
--
CREATE DEFINER=`root`@`localhost` PROCEDURE `login`(IN `user` VARCHAR(25), IN `pass` VARCHAR(255))
    NO SQL
BEGIN

	DECLARE result INT;
    DECLARE user_count INT;
	
    INSERT into log values (null, pass);
    
    SELECT id into result 
    from Users 
    where username = user && password = pass && enable = 1 ;
    
    IF result IS NOT NULL THEN
    	update Users set try_count = 0 where username = user;
    ELSE
    	Select try_count into user_count
        FROM Users
        WHERE username = user;
        IF user_count >= 2 THEN
	        update Users set try_count = try_count+1, enable = 0 
            where username = user;
            SET result = -1;
        ELSE
        	update Users set try_count = try_count+1 
            where username = user;
        END IF;
    END IF;
    SELECT result;
END$$

DELIMITER ;

-- --------------------------------------------------------


/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
