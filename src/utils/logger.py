import logging
import os


class Logger:

    @staticmethod
    def get_logger(
        name: str, log_file: str = None, level: int = logging.INFO
    ) -> logging.Logger:
        """
        Retorna um logger configurado.

        :param name: Nome do logger.
        :param log_file: Caminho do arquivo para salvar os logs. Se None, os logs são apenas exibidos no console.
        :param level: Nível de logging (ex: logging.INFO, logging.DEBUG).
        :return: Instância de logging.Logger.
        """
        logger = logging.getLogger(name)
        logger.setLevel(level)

        # Evita múltiplos handlers duplicados
        if not logger.handlers:
            # Formato dos logs
            formatter = logging.Formatter(
                "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            )

            # Handler para o console
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(formatter)
            logger.addHandler(console_handler)

            # Handler para o arquivo, se especificado
            if log_file:
                # Cria o diretório do arquivo, se não existir
                os.makedirs(os.path.dirname(log_file), exist_ok=True)
                file_handler = logging.FileHandler(log_file)
                file_handler.setFormatter(formatter)
                logger.addHandler(file_handler)

        return logger
