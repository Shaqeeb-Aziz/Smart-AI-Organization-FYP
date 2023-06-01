-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 15, 2023 at 12:46 PM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 7.4.27

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `receptionist`
--

-- --------------------------------------------------------

--
-- Table structure for table `counter`
--

CREATE TABLE `counter` (
  `sr.no` int(5) NOT NULL,
  `date` varchar(11) NOT NULL,
  `token_number` varchar(11) NOT NULL,
  `result` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `counter`
--

INSERT INTO `counter` (`sr.no`, `date`, `token_number`, `result`) VALUES
(1, '2:2:2022', '-1', '2nd interview'),
(2, '12:2:2022', '1', 'Accept'),
(8, '24:2:2022', '1', '2nd interview'),
(9, '1:3:2022', '1', 'internship'),
(10, '1:3:2022', '2', 'internship');

-- --------------------------------------------------------

--
-- Table structure for table `interny_interview`
--

CREATE TABLE `interny_interview` (
  `sr no.` int(3) NOT NULL,
  `Question` varchar(255) NOT NULL,
  `o1` varchar(255) NOT NULL,
  `o2` varchar(255) NOT NULL,
  `o3` varchar(255) NOT NULL,
  `o4` varchar(255) NOT NULL,
  `Answer` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `interny_interview`
--

INSERT INTO `interny_interview` (`sr no.`, `Question`, `o1`, `o2`, `o3`, `o4`, `Answer`) VALUES
(1, 'what is python?', 'Script language', 'Machine language', 'programing language', 'alien language', 'o3'),
(2, 'Why we use numpy?', 'Mathematical operation.', 'Data manipulate.', 'Image Processing', 'Identify images', 'o1'),
(3, 'Why we use Matplotlib?', 'graphical representation of data', 'numerical representation of data', 'physical representation of data', 'decision taken from data', 'o1'),
(4, 'How to flip a image to horizontal? ', 'cv2.flip(img, 0)', 'cv2.flip(img, 1)', 'cv2.flip(img, 2)', 'cv2.flip(img, 3)\r\n', 'o2'),
(5, 'why we use cap.release()?', 'release rescores consume by microphone', 'release resources consume by microphone', 'release speaker function', 'release camera resources', 'o4');

-- --------------------------------------------------------

--
-- Table structure for table `interview`
--

CREATE TABLE `interview` (
  `name` varchar(20) NOT NULL,
  `Gender` varchar(8) NOT NULL,
  `cnic` varchar(13) NOT NULL,
  `date_visit` varchar(10) NOT NULL,
  `education` varchar(20) NOT NULL,
  `institute` varchar(35) NOT NULL,
  `purpose` varchar(100) NOT NULL,
  `ticket` varchar(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `interview_results`
--

CREATE TABLE `interview_results` (
  `sr no.` int(20) NOT NULL,
  `cnic` varchar(13) NOT NULL,
  `name` varchar(35) NOT NULL,
  `date` varchar(11) NOT NULL,
  `experience` varchar(15) NOT NULL,
  `offer` varchar(15) NOT NULL,
  `skill` varchar(50) NOT NULL,
  `exp_sallary` varchar(28) NOT NULL,
  `knowledge` varchar(12) DEFAULT NULL,
  `decision` varchar(18) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `interview_results`
--

INSERT INTO `interview_results` (`sr no.`, `cnic`, `name`, `date`, `experience`, `offer`, `skill`, `exp_sallary`, `knowledge`, `decision`) VALUES
(5, '7897987813215', 'manan', '24:2:2022', 'yes', '2nd interview', 'hard working', '5000', 'poor', '2nd interview'),
(6, '1432142312311', 'alexandra', '1:3:2022', 'none', 'internship', 'hard working', '95000', 'poor', 'reject');

-- --------------------------------------------------------

--
-- Table structure for table `job_interview`
--

CREATE TABLE `job_interview` (
  `sr no.` int(3) NOT NULL,
  `Question` varchar(255) NOT NULL,
  `o1` varchar(255) NOT NULL,
  `o2` varchar(255) NOT NULL,
  `o3` varchar(255) NOT NULL,
  `o4` varchar(255) NOT NULL,
  `Answer` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `job_interview`
--

INSERT INTO `job_interview` (`sr no.`, `Question`, `o1`, `o2`, `o3`, `o4`, `Answer`) VALUES
(1, 'What is used for call 2 or more then 2 function at a same time?', 'Nested function', 'Loop function', 'iterative function', 'Thread function', 'o4'),
(2, 'why we use .h5 file extension? ', 'Html5 short form', 'store Model weights ', 'Allow users to access all network', 'Connect database pacage', 'o2'),
(3, 'What is transformer?', 'NLP SOTA model ', 'Transformer prime ', 'Chat boat app', 'Image processing model', 'o1'),
(4, 'What is the name of the pioneer of AI ', 'Alan Turing', 'Henry sen', 'Job Shn', 'Irnzun Iruna', 'o1'),
(5, 'What is the draw back of threads?', 'if 1 exception is miss it will destroy all the resources until program shut down', 'Conflict with other functions', 'User extra resources ', 'Decrease the efficiency of program', 'o1');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `counter`
--
ALTER TABLE `counter`
  ADD PRIMARY KEY (`sr.no`);

--
-- Indexes for table `interny_interview`
--
ALTER TABLE `interny_interview`
  ADD PRIMARY KEY (`sr no.`);

--
-- Indexes for table `interview`
--
ALTER TABLE `interview`
  ADD PRIMARY KEY (`cnic`);

--
-- Indexes for table `interview_results`
--
ALTER TABLE `interview_results`
  ADD PRIMARY KEY (`sr no.`);

--
-- Indexes for table `job_interview`
--
ALTER TABLE `job_interview`
  ADD PRIMARY KEY (`sr no.`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `counter`
--
ALTER TABLE `counter`
  MODIFY `sr.no` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `interny_interview`
--
ALTER TABLE `interny_interview`
  MODIFY `sr no.` int(3) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `interview_results`
--
ALTER TABLE `interview_results`
  MODIFY `sr no.` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `job_interview`
--
ALTER TABLE `job_interview`
  MODIFY `sr no.` int(3) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
