"""
This example shows how to use jinja2 to generate configuration files for BGP and IPsec VPN.
"""

from configgen import template_loader

def main():
    """ Example """
    # Generate BGP Config
    template_loader("yaml/bgp_conf.yml", "template/bgp_template", "config/bgp.conf")
    # Generate IKEv2 Config
    template_loader("yaml/ikev2_conf.yml", "template/ikev2_template", "config/ikev2.conf")

if __name__ == "__main__":
    main()
