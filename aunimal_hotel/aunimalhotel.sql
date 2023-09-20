-- MySQL Workbench Synchronization
-- Generated: 2023-09-18 15:49
-- Model: New Model
-- Version: 1.0
-- Project: Aunimal Hotel
-- Author: Rafaela Vecchi

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

CREATE SCHEMA IF NOT EXISTS `aunimalassociadohotel` DEFAULT CHARACTER SET utf8mb4 ;

CREATE TABLE IF NOT EXISTS `aunimalhotel`.`cliente` (
  `id_cliente` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `id_associado` INT(10) UNSIGNED NOT NULL,
  PRIMARY KEY (`id_cliente`),
  UNIQUE INDEX `id_associado_UNIQUE` (`id_associado` ASC) VISIBLE,
  CONSTRAINT `fk_associado`
    FOREIGN KEY (`id_associado`)
    REFERENCES `aunimalhotel`.`associado` (`id_associado`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `aunimalhotel`.`cobranca` (
  `id_cobranca` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `data_vencimento` DATETIME NOT NULL,
  `valor_cobranca` DECIMAL(10,2) NOT NULL,
  `id_reserva` INT(10) UNSIGNED NOT NULL,
  PRIMARY KEY (`id_cobranca`),
  INDEX `fk_cobranca_reserva_idx1` (`id_reserva` ASC) VISIBLE,
  UNIQUE INDEX `id_cobranca_UNIQUE` (`id_cobranca` ASC) VISIBLE,
  CONSTRAINT `fk_cobranca_reserva`
    FOREIGN KEY (`id_reserva`)
    REFERENCES `aunimalhotel`.`reserva` (`id_reserva`)
    ON DELETE RESTRICT
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `aunimalhotel`.`contato` (
  `id_contato` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `codigo_pais` INT(10) UNSIGNED ZEROFILL NOT NULL,
  `codigo_area` INT(10) UNSIGNED NOT NULL,
  `numero` BIGINT(19) UNSIGNED NOT NULL,
  `id_associado` INT(10) UNSIGNED NOT NULL,
  PRIMARY KEY (`id_contato`),
  UNIQUE INDEX `id_contato_UNIQUE` (`id_contato` ASC) VISIBLE,
  UNIQUE INDEX `numero_UNIQUE` (`numero` ASC) INVISIBLE,
  INDEX `fk_associado_idx` (`id_associado` ASC) VISIBLE,
  UNIQUE INDEX `id_associado_UNIQUE` (`id_associado` ASC) VISIBLE,
  CONSTRAINT `fk_id_associado`
    FOREIGN KEY (`id_associado`)
    REFERENCES `aunimalhotel`.`associado` (`id_associado`)
    ON DELETE RESTRICT
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `aunimalhotel`.`endereco` (
  `id_endereco` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `cep` CHAR(8) NOT NULL,
  `numero` SMALLINT(5) UNSIGNED NOT NULL,
  `bairro` VARCHAR(50) NOT NULL,
  `cidade` VARCHAR(100) NOT NULL,
  `estado` VARCHAR(100) NOT NULL,
  `id_associado` INT(10) UNSIGNED NOT NULL,
  PRIMARY KEY (`id_endereco`),
  UNIQUE INDEX `id_endereco_UNIQUE` (`id_endereco` ASC) VISIBLE,
  UNIQUE INDEX `id_associado_UNIQUE` (`id_associado` ASC) VISIBLE,
  CONSTRAINT `fkassociados`
    FOREIGN KEY (`id_associado`)
    REFERENCES `aunimalhotel`.`associado` (`id_associado`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci
KEY_BLOCK_SIZE = 1;

CREATE TABLE IF NOT EXISTS `aunimalhotel`.`funcionario` (
  `id_funcionario` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `data_admicao` TIMESTAMP NOT NULL,
  `salario` DECIMAL(10,2) NOT NULL,
  `estado_civil` VARCHAR(45) NOT NULL,
  `id_associado` INT(10) UNSIGNED NOT NULL,
  `id_profissao` INT(10) UNSIGNED NOT NULL,
  PRIMARY KEY (`id_funcionario`),
  UNIQUE INDEX `id_funcionario_UNIQUE` (`id_funcionario` ASC) VISIBLE,
  UNIQUE INDEX `id_profissao_UNIQUE` (`id_profissao` ASC) VISIBLE,
  UNIQUE INDEX `id_associado_UNIQUE` (`id_associado` ASC) VISIBLE,
  CONSTRAINT `fk_id_profissao`
    FOREIGN KEY (`id_profissao`)
    REFERENCES `aunimalhotel`.`profissao` (`id_profissao`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_id_associado_funcionario`
    FOREIGN KEY (`id_associado`)
    REFERENCES `aunimalhotel`.`associado` (`id_associado`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `aunimalhotel`.`pagamento` (
  `id_pagamento` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `valor_a_pagar` DECIMAL(10,2) NOT NULL,
  `data_pagamento` DATETIME NOT NULL,
  `mes_referencia` DATE NOT NULL,
  `id_funcionario` INT(10) UNSIGNED NOT NULL,
  INDEX `fk_pagamento_funcionario_idx` (`id_funcionario` ASC) VISIBLE,
  PRIMARY KEY (`id_pagamento`),
  UNIQUE INDEX `id_pagamento_UNIQUE` (`id_pagamento` ASC) VISIBLE,
  CONSTRAINT `fk_pagamento_funcionario`
    FOREIGN KEY (`id_funcionario`)
    REFERENCES `aunimalhotel`.`funcionario` (`id_funcionario`)
    ON DELETE RESTRICT
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `aunimalhotel`.`associado` (
  `id_associado` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(100) NOT NULL,
  `nascimento` DATE NOT NULL,
  `cpf` CHAR(11) NOT NULL,
  `rg` CHAR(11) NOT NULL,
  `sexo` ENUM('M', 'F', 'NI') NOT NULL,
  `email` VARCHAR(50) NOT NULL,
  `nacionalidade` VARCHAR(100) NOT NULL DEFAULT 'Brasil',
  `data_criacao` TIMESTAMP NOT NULL,
  PRIMARY KEY (`id_associado`),
  UNIQUE INDEX `cpf` (`cpf` ASC) VISIBLE,
  UNIQUE INDEX `rg` (`rg` ASC) VISIBLE,
  UNIQUE INDEX `email` (`email` ASC) VISIBLE,
  UNIQUE INDEX `id_associado_UNIQUE` (`id_associado` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `aunimalhotel`.`pet` (
  `id_pet` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `data_criacao` TIMESTAMP NOT NULL,
  `nome` VARCHAR(50) NOT NULL,
  `peso` DECIMAL(5,2) NOT NULL,
  `sexo` ENUM('M', 'F') NOT NULL,
  `porte` ENUM('PP', 'P', 'M', 'G', 'GG') NOT NULL,
  `nascimento` DATE NOT NULL,
  `descricao` TINYTEXT NULL DEFAULT NULL,
  `id_especie` INT(10) UNSIGNED NOT NULL,
  `id_raca` INT(10) UNSIGNED NOT NULL,
  PRIMARY KEY (`id_pet`),
  INDEX `fk_pet_especie_idx` (`id_especie` ASC) VISIBLE,
  UNIQUE INDEX `id_UNIQUE` (`id_pet` ASC) VISIBLE,
  INDEX `fk_id_raca_idx` (`id_raca` ASC) VISIBLE,
  CONSTRAINT `fk_pet_especie`
    FOREIGN KEY (`id_especie`)
    REFERENCES `aunimalhotel`.`especie` (`id_especie`)
    ON DELETE RESTRICT
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_id_raca`
    FOREIGN KEY (`id_raca`)
    REFERENCES `aunimalhotel`.`raca` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `aunimalhotel`.`servico` (
  `id_servico` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `valor_servico` DECIMAL(10,2) NOT NULL,
  `descricao` TINYTEXT NOT NULL,
  `nome_servico` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id_servico`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;

CREATE TABLE IF NOT EXISTS `aunimalhotel`.`especie` (
  `id_especie` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `tipo` VARCHAR(25) NOT NULL,
  PRIMARY KEY (`id_especie`),
  UNIQUE INDEX `id_especie_UNIQUE` (`id_especie` ASC) VISIBLE,
  UNIQUE INDEX `tipo_UNIQUE` (`tipo` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;

CREATE TABLE IF NOT EXISTS `aunimalhotel`.`raca` (
  `id` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `classificacao` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `classificacao_UNIQUE` (`classificacao` ASC) VISIBLE,
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;

CREATE TABLE IF NOT EXISTS `aunimalhotel`.`reserva` (
  `id_reserva` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `check_in` DATETIME NOT NULL,
  `checkout` DATETIME NOT NULL,
  `descricao` TINYTEXT NULL DEFAULT NULL,
  `valor_total` DECIMAL(10,2) NOT NULL,
  `id_cliente` INT(10) UNSIGNED NOT NULL,
  `id_funcionario` INT(10) UNSIGNED NOT NULL,
  `id_servico` INT(10) UNSIGNED NOT NULL,
  `id_pet` INT(10) UNSIGNED NOT NULL,
  PRIMARY KEY (`id_reserva`),
  INDEX `fk_cliente_reserva_idx` (`id_cliente` ASC) INVISIBLE,
  INDEX `fk_servico_idx` (`id_servico` ASC) VISIBLE,
  INDEX `fk_funcionario_reserva_idx` (`id_funcionario` ASC) VISIBLE,
  INDEX `fk_pet_idx` (`id_pet` ASC) VISIBLE,
  CONSTRAINT `fk_cliente_reserva`
    FOREIGN KEY (`id_cliente`)
    REFERENCES `aunimalhotel`.`cliente` (`id_cliente`)
    ON DELETE RESTRICT
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_funcionario_reserva`
    FOREIGN KEY (`id_funcionario`)
    REFERENCES `aunimalhotel`.`funcionario` (`id_funcionario`)
    ON DELETE RESTRICT
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_servico`
    FOREIGN KEY (`id_servico`)
    REFERENCES `aunimalhotel`.`servico` (`id_servico`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_pet`
    FOREIGN KEY (`id_pet`)
    REFERENCES `aunimalhotel`.`pet` (`id_pet`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;

CREATE TABLE IF NOT EXISTS `aunimalhotel`.`forma` (
  `id_forma` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `formnome_forma_pagamento` VARCHAR(45) NOT NULL,
  `descricao` TINYTEXT NOT NULL,
  PRIMARY KEY (`id_forma`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;

CREATE TABLE IF NOT EXISTS `aunimalhotel`.`cobranca_forma` (
  `id_cobranca_forma` INT(10) UNSIGNED NOT NULL,
  `id_cobranca` INT(10) UNSIGNED NOT NULL,
  `id_forma` INT(10) UNSIGNED NOT NULL,
  INDEX `fk_cobranca_forma_cobranca_idx` (`id_cobranca` ASC) VISIBLE,
  INDEX `fk_cobranca_forma_forma_idx` (`id_forma` ASC) VISIBLE,
  PRIMARY KEY (`id_cobranca_forma`),
  UNIQUE INDEX `id_cobranca_forma_UNIQUE` (`id_cobranca_forma` ASC) VISIBLE,
  CONSTRAINT `fk_cobranca_forma_cobranca`
    FOREIGN KEY (`id_cobranca`)
    REFERENCES `aunimalhotel`.`cobranca` (`id_cobranca`)
    ON DELETE RESTRICT
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_cobranca_forma_forma`
    FOREIGN KEY (`id_forma`)
    REFERENCES `aunimalhotel`.`forma` (`id_forma`)
    ON DELETE RESTRICT
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;

CREATE TABLE IF NOT EXISTS `aunimalhotel`.`profissao` (
  `id_profissao` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `profissao` VARCHAR(45) NOT NULL,
  `descricao` TINYTEXT NULL DEFAULT NULL,
  PRIMARY KEY (`id_profissao`),
  UNIQUE INDEX `id_profissao_UNIQUE` (`id_profissao` ASC) VISIBLE,
  UNIQUE INDEX `profissao_UNIQUE` (`profissao` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
