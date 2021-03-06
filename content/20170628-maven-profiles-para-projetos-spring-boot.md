---
layout: post
title:  Maven Profiles para Projetos Spring-Boot
date:   2017-06-29
category: Spring
image: /images/spring.png
---

Neste post iremos mostrar como usar de maneira fácil os Maven Profiles em conjunto com o Maven Resources para controlar as versões de uma aplicação em cada ambiente.

##O Problema

Ao lidar com a migração de sistemas entre **DEV**, **QAS** e **PRD** muitas vezes esbarramos na configuração de váriações de acordo com o ambiente.

Em projetos Spring Boot rodados como Boot projects (`java -jar projeto.jar`) configuramos inumeros application.properties, um para cada ambiente (ex.: `application-dev.properties`). Então ao rodar o projeto informa-se o profile escolhido (`java -jar -Dspring.profiles.active=dev projeto.jar`).

**Mais informações em:** <https://docs.spring.io/spring-boot/docs/current/reference/html/howto-properties-and-configuration.html#howto-change-configuration-depending-on-the-environment>

O problema neste caso é que muitas vezes temos que hospedar o projeto em outros servidores, de modo que não podemos utilizar o seu boot initializer. Sendo assim o que fazer?

Uma saída é utilizar o **Maven Profiles** em conjunto com o **Maven Resources**. Com o **Maven Profiles** conseguimos criar variáveis de acordo com o ambiente e com o **Resources** conseguimos subistituir essas variáveis nos arquivos de configuração do **Spring Boot**.

##[Spring Boot Actuator](https://github.com/spring-projects/spring-boot/tree/master/spring-boot-actuator)

Primeiramente adicionaremos o actuator como uma dependência do nosso projeto:

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-actuator</artifactId>
</dependency>
```

O Actuator irá disponibilizar alguns endpoints já 'prontos' para nosso projeto, incluindo o `/info` que usaremos posteriormente.

##[Maven Profiles](http://maven.apache.org/guides/introduction/introduction-to-profiles.html)

Maven Profiles é a maneira que maven permite que definamos variáveis e caminhos para o build dependendo do perfil selecionado. No nosso caso configuramos **DEV**, **QAS** e **PRD**:

```xml
<profiles>
    <profile>
        <id>dev</id>
        <properties>
            <app.environment.label>DEV</app.environment.label>
            <app.auth.server.address>server.dev.br</app.auth.server.address>
            <app.auth.server.port>8080</app.auth.server.port>
        </properties>
    </profile>
    <profile>
        <id>qas</id>
        <properties>
            <app.environment.label>QAS</app.environment.label>
            <app.auth.server.address>server.qas.br</app.auth.server.address>
            <app.auth.server.port>80</app.auth.server.port>
        </properties>
    </profile>
    <profile>
        <id>prd</id>
        <properties>
            <app.environment.label>PRD</app.environment.label>
            <app.auth.server.address>server.prd.br</app.auth.server.address>
            <app.auth.server.port>80</app.auth.server.port>
        </properties>
    </profile>
</profiles>
```

Para cada profile definimos 3 variáveis: o label do ambiente (`app.environment.label`), o endereço (`app.auth.server.address`) e porta (`app.auth.server.port`) do servidor de autenticação. Sendo assim quando rodarmos o build do maven (`mvn clean install -P<profile>`) informamos qual o profile a ser utilizado. Temos a opção de colocar a tag `activation` dentro de um profile o definindo como o padrão caso nenhum seja fornecido:

```xml
<activation>
    <activeByDefault>true</activeByDefault>
</activation>
```

Com as variáveis definidas precisamos agora utilizalas pelo Spring. É ai que o **Maven Resources** entra em ação.

##[Maven Resources](https://maven.apache.org/plugins/maven-resources-plugin/)

O **Maven Resources** é um plugin com inumeras utilidades que age principalmente sobre os recursos da aplicação, renomeando, mudando de lugar e até subistituindo o conteúdo de arquivos de acordo com padrões, que é justamente o que precisamos.

```xml
<build>
    <finalName>projeto</finalName>
    <plugins>
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-resources-plugin</artifactId>
            <configuration>
                <delimiters>
                    <delimiter>@</delimiter>
                </delimiters>
                <resources>
                    <resource>
                        <directory>src/main/resources</directory>
                        <filtering>true</filtering>
                    </resource>
                </resources>
            </configuration>
        </plugin>
        ...
    </plugins>
</build>
```

Essa configuração informa para o plugin que ele deve ler todos os arquivos dentro de `src/main/resources` e subistituir tudo que for delimitado por `@`. Ex.: `@property.replace@`

##Spring Boot [application.properties](https://docs.spring.io/spring-boot/docs/current/reference/html/common-application-properties.html)

Dentro do `application.properties` iremos utilizar as 3 variáveis criadas pelos profiles. Para isso colocaremo-as como filhas da propriedade `info` que por padrão joga todo o seu conteúdo como JSON através do endpoint `/info` fornecido pelo actuator:

```
server.port=9000

info.environment=@app.environment.label@
info.auth.server=@app.auth.server.address@:@app.auth.server.port@
```

* Definimos a porta da aplicação para 9000 para evitar conflitos na 8080.
* Na propriedade `environment` exibiremos o label do ambiente.
* Na propriedade `auth.server` exibiremos o endereço do servidor e porta.

##Testando

Execute o projeto como spring-boot passando `dev` como profile (`-P`)

```
mvn spring-boot:run -Pdev
```

Acesse <http://localhost:9000/info>

![Resultado do teste](/images/20170628/test.jpg)

Agora realize o mesmo procedimento para **QAS** e **PRD**.

##Código Fonte 
<a href="https://github.com/pedrohrr/fullstackninja.com.br/tree/master/projects/maven-profiles-resources" class="btn btn-success">
	GitHub
</a>
