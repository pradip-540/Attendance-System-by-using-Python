-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 02, 2023 at 07:07 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `attendance_gui`
--

-- --------------------------------------------------------

--
-- Table structure for table `bca_d`
--

CREATE TABLE `bca_d` (
  `sEnroll` varchar(100) NOT NULL,
  `sName` varchar(100) NOT NULL,
  `sRoll` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `bca_d`
--

INSERT INTO `bca_d` (`sEnroll`, `sName`, `sRoll`) VALUES
('22SOEBCA11001', 'Krishna Dev ', '1'),
('22SOEBCA11002', 'Surya Karn', '2'),
('22SOEBCA11003', 'Vishnu Gupta', '3'),
('22SOEBCA11004', 'Candra Gupta Maurya', '4'),
('22SOEBCA11005', 'Vikram Aditya', '5');

-- --------------------------------------------------------

--
-- Table structure for table `bca_d_os`
--

CREATE TABLE `bca_d_os` (
  `date` varchar(100) NOT NULL,
  `sEnroll` varchar(100) NOT NULL,
  `sName` varchar(100) NOT NULL,
  `sRoll` varchar(100) NOT NULL,
  `status` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `bca_d_python`
--

CREATE TABLE `bca_d_python` (
  `date` varchar(100) NOT NULL,
  `sEnroll` varchar(100) NOT NULL,
  `sName` varchar(100) NOT NULL,
  `sRoll` varchar(100) NOT NULL,
  `status` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `ce_d`
--

CREATE TABLE `ce_d` (
  `sEnroll` varchar(100) NOT NULL,
  `sName` varchar(100) NOT NULL,
  `sRoll` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `ce_d_os`
--

CREATE TABLE `ce_d_os` (
  `date` varchar(100) NOT NULL,
  `sEnroll` varchar(100) NOT NULL,
  `sName` varchar(100) NOT NULL,
  `sRoll` varchar(100) NOT NULL,
  `status` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `ce_d_python`
--

CREATE TABLE `ce_d_python` (
  `date` varchar(100) NOT NULL,
  `sEnroll` varchar(100) NOT NULL,
  `sName` varchar(100) NOT NULL,
  `sRoll` varchar(100) NOT NULL,
  `status` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
