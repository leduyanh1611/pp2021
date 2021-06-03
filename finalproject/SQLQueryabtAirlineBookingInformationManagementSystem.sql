USE [master]
GO

/****** Object:  Database [AirlineBookingInformationManagementSystem]    Script Date: 6/4/2021 2:13:33 AM ******/
CREATE DATABASE [AirlineBookingInformationManagementSystem]
 CONTAINMENT = NONE
 ON  PRIMARY 
( NAME = N'AirlineBookingInformationManagementSystem', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL15.DUYANH\MSSQL\DATA\AirlineBookingInformationManagementSystem.mdf' , SIZE = 8192KB , MAXSIZE = UNLIMITED, FILEGROWTH = 65536KB )
 LOG ON 
( NAME = N'AirlineBookingInformationManagementSystem_log', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL15.DUYANH\MSSQL\DATA\AirlineBookingInformationManagementSystem_log.ldf' , SIZE = 8192KB , MAXSIZE = 2048GB , FILEGROWTH = 65536KB )
 WITH CATALOG_COLLATION = DATABASE_DEFAULT
GO

IF (1 = FULLTEXTSERVICEPROPERTY('IsFullTextInstalled'))
begin
EXEC [AirlineBookingInformationManagementSystem].[dbo].[sp_fulltext_database] @action = 'enable'
end
GO

ALTER DATABASE [AirlineBookingInformationManagementSystem] SET ANSI_NULL_DEFAULT OFF 
GO

ALTER DATABASE [AirlineBookingInformationManagementSystem] SET ANSI_NULLS OFF 
GO

ALTER DATABASE [AirlineBookingInformationManagementSystem] SET ANSI_PADDING OFF 
GO

ALTER DATABASE [AirlineBookingInformationManagementSystem] SET ANSI_WARNINGS OFF 
GO

ALTER DATABASE [AirlineBookingInformationManagementSystem] SET ARITHABORT OFF 
GO

ALTER DATABASE [AirlineBookingInformationManagementSystem] SET AUTO_CLOSE OFF 
GO

ALTER DATABASE [AirlineBookingInformationManagementSystem] SET AUTO_SHRINK OFF 
GO

ALTER DATABASE [AirlineBookingInformationManagementSystem] SET AUTO_UPDATE_STATISTICS ON 
GO

ALTER DATABASE [AirlineBookingInformationManagementSystem] SET CURSOR_CLOSE_ON_COMMIT OFF 
GO

ALTER DATABASE [AirlineBookingInformationManagementSystem] SET CURSOR_DEFAULT  GLOBAL 
GO

ALTER DATABASE [AirlineBookingInformationManagementSystem] SET CONCAT_NULL_YIELDS_NULL OFF 
GO

ALTER DATABASE [AirlineBookingInformationManagementSystem] SET NUMERIC_ROUNDABORT OFF 
GO

ALTER DATABASE [AirlineBookingInformationManagementSystem] SET QUOTED_IDENTIFIER OFF 
GO

ALTER DATABASE [AirlineBookingInformationManagementSystem] SET RECURSIVE_TRIGGERS OFF 
GO

ALTER DATABASE [AirlineBookingInformationManagementSystem] SET  ENABLE_BROKER 
GO

ALTER DATABASE [AirlineBookingInformationManagementSystem] SET AUTO_UPDATE_STATISTICS_ASYNC OFF 
GO

ALTER DATABASE [AirlineBookingInformationManagementSystem] SET DATE_CORRELATION_OPTIMIZATION OFF 
GO

ALTER DATABASE [AirlineBookingInformationManagementSystem] SET TRUSTWORTHY OFF 
GO

ALTER DATABASE [AirlineBookingInformationManagementSystem] SET ALLOW_SNAPSHOT_ISOLATION OFF 
GO

ALTER DATABASE [AirlineBookingInformationManagementSystem] SET PARAMETERIZATION SIMPLE 
GO

ALTER DATABASE [AirlineBookingInformationManagementSystem] SET READ_COMMITTED_SNAPSHOT OFF 
GO

ALTER DATABASE [AirlineBookingInformationManagementSystem] SET HONOR_BROKER_PRIORITY OFF 
GO

ALTER DATABASE [AirlineBookingInformationManagementSystem] SET RECOVERY FULL 
GO

ALTER DATABASE [AirlineBookingInformationManagementSystem] SET  MULTI_USER 
GO

ALTER DATABASE [AirlineBookingInformationManagementSystem] SET PAGE_VERIFY CHECKSUM  
GO

ALTER DATABASE [AirlineBookingInformationManagementSystem] SET DB_CHAINING OFF 
GO

ALTER DATABASE [AirlineBookingInformationManagementSystem] SET FILESTREAM( NON_TRANSACTED_ACCESS = OFF ) 
GO

ALTER DATABASE [AirlineBookingInformationManagementSystem] SET TARGET_RECOVERY_TIME = 60 SECONDS 
GO

ALTER DATABASE [AirlineBookingInformationManagementSystem] SET DELAYED_DURABILITY = DISABLED 
GO

ALTER DATABASE [AirlineBookingInformationManagementSystem] SET ACCELERATED_DATABASE_RECOVERY = OFF  
GO

ALTER DATABASE [AirlineBookingInformationManagementSystem] SET QUERY_STORE = OFF
GO

ALTER DATABASE [AirlineBookingInformationManagementSystem] SET  READ_WRITE 
GO


