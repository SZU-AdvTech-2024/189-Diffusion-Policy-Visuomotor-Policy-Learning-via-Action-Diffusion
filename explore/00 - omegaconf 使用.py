import hydra
from omegaconf import OmegaConf

@hydra.main(
    version_base=None,
    config_path="../train_config",
    config_name="my_cnn_pusht.yaml"
)
def main(cfg: OmegaConf):
    # resolve immediately so all the ${now:} resolvers
    # will use the same time.
    OmegaConf.resolve(cfg)
    print(cfg)



if __name__ == "__main__":
    main()
